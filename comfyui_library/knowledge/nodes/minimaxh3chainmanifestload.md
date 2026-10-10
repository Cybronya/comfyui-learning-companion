# MiniMaxH3ChainManifestLoad

## 节点类型

`MiniMaxH3ChainManifestLoad`

## 分类

Input

## 作用

输入类节点：读入外部数据（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `plan:H3_CHAIN_PLAN`（1 次）
- `source_audio:AUDIO`（1 次）
- `external_context:H3_CHAIN_EXTERNAL_CONTEXT`（1 次）
- `source_timeline:H3_SOURCE_TIMELINE`（1 次）

## 输出

- `manifest:H3_CHAIN_MANIFEST`（1 次）
- `manifest_json:STRING`（1 次）
- `status:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
