# UploadToImageHost

## 节点类型

`UploadToImageHost`

## 分类

Input

## 作用

输入类节点：读入外部数据（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（1 次）
- `upload_url:STRING`（1 次）
- `format:COMBO`（1 次）
- `quality:INT`（1 次）
- `timeout:INT`（1 次）

## 输出

- `图片URL:STRING`（1 次）
- `创建时间:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["https://imageproxy.zhongzhuan.chat/api/upload", "jpeg", 95, 120]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
