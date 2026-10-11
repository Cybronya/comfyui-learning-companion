# LtoJ_H3ReferenceVideoUpload

## 节点类型

`LtoJ_H3ReferenceVideoUpload`

## 分类

Input

## 作用

输入类节点：读入外部数据（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `video:COMBO`（3 次）
- `enabled:BOOLEAN`（3 次）
- `include_audio:BOOLEAN`（3 次）
- `role:COMBO`（3 次）
- `upload:IMAGEUPLOAD`（3 次）

## 输出

- `参考视频与启用状态:LTOJ_H3_VIDEO_REFERENCE_ITEM`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["未选择视频", false, false, "动作与节奏", "image", "image"]`（3 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
