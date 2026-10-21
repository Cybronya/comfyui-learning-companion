---
name: unknown_workflow_video_lora_clip_2
type: Unknown Workflow
frequency: 16
level: strong
coverage: 0.819625
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CR Text, Fast Muter (rgthree), GetNode, ImpactInt, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, MathExpression|pysssss, ModelPatchTorchSettings, ModelSamplingSD3, Mute / Bypass Repeater (rgthree), PathchSageAttentionKJ, RIFE VFI, SetNode, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, wanBlockSwap]
problems: []
missing: []
members: [视频生成/图生视频/1996391603323412482.json, 视频生成/图生视频/1991311451711209474.json, 视频生成/图生视频/1997224219001950210.json, 视频生成/图生视频/2056912993627238401.json, 视频生成/图生视频/2063808011449233410.json, 视频生成/图生视频/1991461571396321281.json, 视频生成/图生视频/1991460751665741826.json, 视频生成/图生视频/1991461490997862402.json, 视频生成/图生视频/WAN22 REMIX V2 首-中-尾三帧视频_1990697911728168962.json, 视频生成/图生视频/1991455227079520257.json, 视频生成/图生视频/2065456197679017986.json, 视频生成/图生视频/1989123289857527809.json, 视频生成/图生视频/1993472274546229249.json, 视频生成/图生视频/1991285079978672130.json, 视频生成/图生视频/1988858056983318530.json, 视频生成/图生视频/1988891469786263553.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_clip_2

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（视频生成/图生视频/1996391603323412482.json、视频生成/图生视频/1991311451711209474.json、视频生成/图生视频/1997224219001950210.json、视频生成/图生视频/2056912993627238401.json、视频生成/图生视频/2063808011449233410.json…）

- **类型**：Unknown Workflow
- **样本数**：16
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 16 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CR Text`
- `Fast Muter (rgthree)`
- `GetNode`
- `ImpactInt`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MathExpression|pysssss`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `Mute / Bypass Repeater (rgthree)`
- `PathchSageAttentionKJ`
- `RIFE VFI`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `wanBlockSwap`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJ` —— 15/16 个有
- `easy getNode` —— 14/16 个有
- `easy setNode` —— 14/16 个有
- `KSamplerAdvanced` —— 12/16 个有
- `WanFirstMiddleLastFrameToVideo` —— 12/16 个有
- `WanMoeKSampler` —— 4/16 个有
- `WanFirstLastFrameToVideo` —— 3/16 个有
- `Note Plus (mtb)` —— 2/16 个有
- `AILab_QwenVL` —— 1/16 个有
- `CR Text Replace` —— 1/16 个有
- `JjkText` —— 1/16 个有
- `PainterI2V` —— 1/16 个有
- `PreviewAny` —— 1/16 个有
- `PrimitiveBoolean` —— 1/16 个有
- `TextBox` —— 1/16 个有
- `easy ifElse` —— 1/16 个有
- `孤海注释` —— 1/16 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 16 | 100% |
| Prompt 约束强度(CFG) | 5 | 5 - 6 | 16 | 92% |
| 采样算法 | 1 | 1 - 1 | 16 | 100% |
| 调度器 | euler | - | 16 | 75% |
| 重绘幅度 | simple | - | 16 | 75% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，16 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 5，观测区间 5 - 6，16 个样本，取值集中（一致性 92%）
- 采样算法 中位数 1，观测区间 1 - 1，16 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，16 个样本，一致性 75%
- 重绘幅度 最常用 simple，16 个样本，一致性 75%
