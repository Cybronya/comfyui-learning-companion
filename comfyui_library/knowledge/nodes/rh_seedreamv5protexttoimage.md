# RH_SeedreamV5ProTextToImage

## 节点类型

`RH_SeedreamV5ProTextToImage`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `api_config:RH_OPENAPI_CONFIG`（1 次）
- `prompt:STRING`（1 次）
- `width:INT`（1 次）
- `height:INT`（1 次）
- `resolution:COMBO`（1 次）
- `outputFormat:COMBO`（1 次）
- `skip_error:BOOLEAN`（1 次）
- `seed:INT`（1 次）

## 输出

- `image:IMAGE`（1 次）
- `url:STRING`（1 次）
- `response:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["直播带货人像，年轻东亚甜美女神，浅棕大波浪长发，精致清透淡妆，温柔微笑看向镜头。身穿棕白蓝条纹无袖Polo针织背心，白色半身短裙。双手托举一双米白色德训小白鞋，鞋子清晰突出。背景是简约白色北欧风室内空间，纯白墙面，浅木色极简软装，干净明`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
