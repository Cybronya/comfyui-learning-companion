# RH_RhartImageG25FlareTextToImage

## 节点类型

`RH_RhartImageG25FlareTextToImage`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `api_config:RH_OPENAPI_CONFIG`（2 次）
- `prompt:STRING`（2 次）
- `aspectRatio:COMBO`（2 次）
- `resolution:COMBO`（2 次）
- `skip_error:BOOLEAN`（2 次）
- `seed:INT`（2 次）

## 输出

- `image:IMAGE`（2 次）
- `url:STRING`（2 次）
- `response:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["一位非常漂亮的东方女子", "16:9", "1k", false, 2069092291, "randomize"]`（1 次）
- `["商业儿童服装棚拍摄影，8K 超高清，超高细节，照片级写实实拍质感，纯色影棚场景。画面中有两名白人肤色欧美小朋友并排站立，左侧小男孩，蓬松卷曲金色短发；右侧小女孩，顺直浅金色长发。孩童正面朝向镜头，身体直立，双臂自然垂于身体两侧，双手放松`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
