# LoadVideo

## 节点类型

`LoadVideo`

## 分类

Input

## 作用

输入类节点：读入外部数据（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 11 个 workflow 中。

## 输入

- `file:COMBO`（11 次）
- `keep_audio:BOOLEAN`（11 次）
- `trim_time:STRING`（11 次）
- `upload:IMAGEUPLOAD`（11 次）

## 输出

- `VIDEO:VIDEO`（11 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["580816394edd75a83643c90a5574ffa6da6e465537f81e78d2ca86f22818d360.mp4", "image", "0", "image"]`（3 次）
- `["80cd89c3b271533f73de751911b4e37f0ba76371eed5f8ed0aea938cb19e4c09.mp4", "image", "0", "image"]`（2 次）
- `["499a9d1726fa338d16b9338421705a6f127c3eeadfd6a2d38759050e7597f354.mp4", true, "0", "image"]`（1 次）
- `["b8929b66c32fe95558e172ea0579a9b7d9840d70decd8d102226403b29621505.mp4", true, "0", "image"]`（1 次）
- `["45398e7a98a85f8ac5f119ad12e0e50deec196c5d56f3f28950da8daa8347350.mp4", true, "0", "image"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
