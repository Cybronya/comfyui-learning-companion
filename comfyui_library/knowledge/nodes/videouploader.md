# VideoUploader

## 节点类型

`VideoUploader`

## 分类

Model Loading

## 作用

加载类节点：把磁盘上的资源装入图中（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `upload:STRING`（1 次）
- `upload_status:STRING`（1 次）

## 输出

- `视频路径:STRING`（1 次）
- `视频信息:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["e6759fdeeed467390221b3b53efe1acdc14afdacda988405f15d5e476f1582c3.mp4", "success", "video"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
