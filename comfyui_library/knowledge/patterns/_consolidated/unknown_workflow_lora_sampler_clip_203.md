---
name: unknown_workflow_lora_sampler_clip_203
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.8715
common_nodes: [BasicScheduler, BatchImagesNode, BerniniConditioning, CLIPLoader, CLIPTextEncode, KSamplerSelect, LoadImage, LoraLoaderModelOnly, PathchSageAttentionKJ, SamplerCustom, SplitSigmas, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoInfo]
problems: []
missing: []
members: [平台全量/Bernini 参考图视频编辑_2062483604135047170.json, 平台全量/Bernini 开源效果！多图参考 + 人物替换_2062410700735213570.json, 平台全量/Bernini 视频编辑模型 一句话改变视频 换人物换背景_2069582307207503873.json, 视频生成/文生视频/Bernini 视频编辑模型 一句话改变视频 RV2V 模式 换人物换背景_2062391464264560641.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_203

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/Bernini 参考图视频编辑_2062483604135047170.json、平台全量/Bernini 开源效果！多图参考 + 人物替换_2062410700735213570.json、平台全量/Bernini 视频编辑模型 一句话改变视频 换人物换背景_2069582307207503873.json、视频生成/文生视频/Bernini 视频编辑模型 一句话改变视频 RV2V 模式 换人物换背景_2062391464264560641.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicScheduler`
- `BatchImagesNode`
- `BerniniConditioning`
- `CLIPLoader`
- `CLIPTextEncode`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PathchSageAttentionKJ`
- `SamplerCustom`
- `SplitSigmas`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoInfo`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 3/4 个有
- `SaveVideo` —— 3/4 个有
- `CR Text` —— 2/4 个有
- `ImpactInt` —— 2/4 个有
- `SimpleMath+` —— 2/4 个有
- `StringFunction|pysssss` —— 2/4 个有
- `VHS_VideoCombine` —— 2/4 个有
- `孤海注释` —— 2/4 个有
- `CM_IntToFloat` —— 1/4 个有
- `INTConstant` —— 1/4 个有
- `ImageResizeKJv2` —— 1/4 个有
- `Note Plus (mtb)` —— 1/4 个有
- `PrimitiveInt` —— 1/4 个有
- `easy imageScaleDownToSize` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
