# Ideogram4PromptBuilderKJ

## 节点类型

`Ideogram4PromptBuilderKJ`

## 分类

Prompt

## 作用

提示词处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（1 次）
- `import_json:STRING`（1 次）
- `width:INT`（1 次）
- `height:INT`（1 次）
- `high_level_description:STRING`（1 次）
- `background:STRING`（1 次）
- `style:COMFY_DYNAMICCOMBO_V3`（1 次）
- `aesthetics:STRING`（1 次）
- `lighting:STRING`（1 次）
- `medium:STRING`（1 次）

## 输出

- `prompt:STRING`（1 次）
- `preview:IMAGE`（1 次）
- `bboxes:BOUNDING_BOX`（1 次）
- `width:INT`（1 次）
- `height:INT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[1928, 1088, "", "", "none", "", "", "", "", "[{\"x\":0.17603058193579285,\"y\":0.07483059007475908,\"w\":0.673440953726`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
