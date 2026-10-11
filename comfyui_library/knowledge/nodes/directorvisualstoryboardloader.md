# DirectorVisualStoryboardLoader

## 节点类型

`DirectorVisualStoryboardLoader`

## 分类

Model Loading

## 作用

加载类节点：把磁盘上的资源装入图中（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `visual_json:STRING`（3 次）
- `cast_dict:DICT`（3 次）

## 输出

- `画面提示词列表(Visual):STRING`（3 次）
- `角色1图:IMAGE`（3 次）
- `角色2图:IMAGE`（3 次）
- `角色3图:IMAGE`（3 次）
- `角色4图:IMAGE`（3 次）
- `角色5图:IMAGE`（3 次）
- `角色6图:IMAGE`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[]`（3 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
