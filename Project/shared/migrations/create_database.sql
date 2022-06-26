CREATE TABLE `users` (
  `id_user` int PRIMARY KEY AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(60) NOT NULL,
  `created_at` datetime NOT NULL DEFAULT (now()),
  `updated_at` datetime NOT NULL DEFAULT (now()),
  `deleted_at` datetime
);

CREATE TABLE `publications` (
  `id_publication` int PRIMARY KEY AUTO_INCREMENT,
  `id_user` int NOT NULL, 
  `id_group` int NOT NULL,
  `content` varchar(255) NOT NULL,
  `created_at` datetime NOT NULL DEFAULT (now()),
  `updated_at` datetime NOT NULL DEFAULT (now()),
  `deleted_at` datetime
);

CREATE TABLE `comments` (
  `id_comment` int PRIMARY KEY AUTO_INCREMENT,
  `id_user` int NOT NULL,
  `id_publication` int,
  `content` varchar(255) NOT NULL,
  `created_at` datetime NOT NULL DEFAULT (now()),
  `updated_at` datetime NOT NULL DEFAULT (now()),
  `deleted_at` datetime
);

CREATE TABLE `tags` (
  `id_tag` int PRIMARY KEY AUTO_INCREMENT,
  `text` varchar(30) NOT NULL
);

CREATE TABLE publications_tags (
  `id_publication` int,
  `id_tag` int
);

CREATE TABLE `likes` (
  `id_user` int,
  `id_publication` int
);

CREATE TABLE `images` (
  `id_image` int PRIMARY KEY AUTO_INCREMENT,
  `url` varchar(255) NOT NULL,
  `created_at` datetime NOT NULL DEFAULT (now()),
  `updated_at` datetime NOT NULL DEFAULT (now()),
  `deleted_at` datetime
);

CREATE TABLE `user_profile_images` (
  `id_user` int,
  `id_image` int,
  `status` int
);

CREATE TABLE `publication_images` (
  `id_publication` int,
  `id_image` int
);

CREATE TABLE `groups_network` (
  `id_group` int PRIMARY KEY AUTO_INCREMENT,
  `name` varchar(255) NOT NULL
);

CREATE TABLE `users_groups` (
  `id_user` int,
  `id_group` int
);

CREATE TABLE `sessions` (
  `id_session` int PRIMARY KEY AUTO_INCREMENT,
  `id_user` int,
  `started_in` datetime NOT NULL DEFAULT (now()),
  `expired_in` datetime NOT NULL
);

ALTER TABLE `publications` ADD FOREIGN KEY (`id_user`) REFERENCES `users` (`id_user`);

ALTER TABLE `comments` ADD FOREIGN KEY (`id_user`) REFERENCES `users` (`id_user`);

ALTER TABLE `comments` ADD FOREIGN KEY (`id_publication`) REFERENCES `publications` (`id_publication`);

ALTER TABLE `likes` ADD FOREIGN KEY (`id_user`) REFERENCES `users` (`id_user`);

ALTER TABLE `likes` ADD FOREIGN KEY (`id_publication`) REFERENCES `publications` (`id_publication`);

ALTER TABLE `user_profile_images` ADD FOREIGN KEY (`id_user`) REFERENCES `users` (`id_user`);

ALTER TABLE `user_profile_images` ADD FOREIGN KEY (`id_image`) REFERENCES `images` (`id_image`);

ALTER TABLE `publication_images` ADD FOREIGN KEY (`id_publication`) REFERENCES `publications` (`id_publication`);

ALTER TABLE `publication_images` ADD FOREIGN KEY (`id_image`) REFERENCES `images` (`id_image`);

ALTER TABLE `sessions` ADD FOREIGN KEY (`id_user`) REFERENCES `users` (`id_user`);

alter view searchPublications as
select p.id_publication,gn.id_group,gn.name as group_name,p.created_at as date, p.content,count(l.id_publication) as likes  from publications p 
inner join groups_network gn on gn.id_group = p.id_group 
inner join publications_tags pt on pt.id_publication = p.id_publication 
left join likes l on l.id_publication = p.id_publication 
group by p.id_publication,gn.name, p.created_at, p.content,l.id_publication 