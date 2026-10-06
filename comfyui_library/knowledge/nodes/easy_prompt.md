# easy prompt

## 节点类型

`easy prompt`

## 分类

Prompt

## 作用

提示词处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `text:STRING`（3 次）
- `prefix:COMBO`（3 次）
- `subject:COMBO`（3 次）
- `action:COMBO`（3 次）
- `clothes:COMBO`（3 次）
- `environment:COMBO`（3 次）
- `background:COMBO`（3 次）
- `nsfw:COMBO`（3 次）

## 输出

- `prompt:STRING`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["The image is a vertical cinematic photograph of a young woman standing on a subway platform, the background and its pa`（3 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
