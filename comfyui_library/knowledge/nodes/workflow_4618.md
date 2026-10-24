# workflow>图片预处理

## 节点类型

`workflow>图片预处理`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `ref_image:IMAGE`（1 次）
- `image:IMAGE`（1 次）
- `latent:LATENT`（1 次）
- `Text:STRING`（1 次）
- `DF_Text_Box Text:STRING`（1 次）
- `api_baseurl:STRING`（1 次）
- `api_key:STRING`（1 次）
- `model:STRING`（1 次）
- `role:STRING`（1 次）
- `prompt:STRING`（1 次）

## 输出

- `width:INT`（1 次）
- `height:INT`（1 次）
- `output:*`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["修改图1的", "的姿势", "", "", "", "识别图中的占图片比例最大的人物并用一个中文词告诉我", "Hello", 0.6, 2013, "randomize", 0, "", "", ""]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
