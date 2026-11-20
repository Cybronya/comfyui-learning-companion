---
name: unknown_workflow_video_lora_clip_4
type: Unknown Workflow
frequency: 12
level: strong
coverage: 0.807167
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CR Text, GetNode, ImpactInt, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, MathExpression|pysssss, ModelPatchTorchSettings, ModelSamplingSD3, Mute / Bypass Repeater (rgthree), PathchSageAttentionKJ, RIFE VFI, SetNode, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/EMIX 首-中-尾三帧生成视频 Wan2.2 反推提示词 Remix 图生视频 REMIX_1996391603323412482.json, 视频生成/图生视频/EMIX++首-中-尾三帧视频  Wan2.2反推提示词-Remix图生视频 REMIX 提示词全自_1991311451711209474.json, 视频生成/图生视频/EMIX++首-中-尾三帧视频  Wan2.2反推提示词-Remix图生视频 REMIX 提示词全自_1997224219001950210.json, 视频生成/图生视频/EMIX++首-中-尾三帧视频++Wan2.2反推提示词-Remix图生视频+REMIX+提示词全自_2056912993627238401.json, 视频生成/图生视频/EMIX++首-中-尾三帧视频_2063808011449233410.json, 视频生成/图生视频/REMIX V2  首-中-尾三帧视频【可】_1991461571396321281.json, 视频生成/图生视频/REMIX V2 -图生视频+ QwenVL图片反推自动提示词_1991460751665741826.json, 视频生成/图生视频/REMIX V2 -最强首尾帧视频-插帧补帧_1991461490997862402.json, 视频生成/图生视频/视频首尾帧_1999869962674204673.json, 视频生成/图生视频/🕵🏻REMIX V2 最强首尾帧视频_1991285079978672130.json, 视频生成/图生视频/🕵🏻大丝袜 动漫专属模型 Dasiwa 图生视频🕵🏻_2007995692123426818.json, 视频生成/图生视频/🕵🏻大丝袜 动漫专属模型 Dasiwa 首尾帧视频🕵🏻_2008006375305125889.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_clip_4

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/图生视频/EMIX 首-中-尾三帧生成视频 Wan2.2 反推提示词 Remix 图生视频 REMIX_1996391603323412482.json、视频生成/图生视频/EMIX++首-中-尾三帧视频  Wan2.2反推提示词-Remix图生视频 REMIX 提示词全自_1991311451711209474.json、视频生成/图生视频/EMIX++首-中-尾三帧视频  Wan2.2反推提示词-Remix图生视频 REMIX 提示词全自_1997224219001950210.json、视频生成/图生视频/EMIX++首-中-尾三帧视频++Wan2.2反推提示词-Remix图生视频+REMIX+提示词全自_2056912993627238401.json、视频生成/图生视频/EMIX++首-中-尾三帧视频_2063808011449233410.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CR Text`
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

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJ` —— 10/12 个有
- `easy getNode` —— 10/12 个有
- `easy setNode` —— 10/12 个有
- `wanBlockSwap` —— 10/12 个有
- `Fast Muter (rgthree)` —— 9/12 个有
- `KSamplerAdvanced` —— 6/12 个有
- `WanFirstMiddleLastFrameToVideo` —— 6/12 个有
- `WanMoeKSampler` —— 6/12 个有
- `WanFirstLastFrameToVideo` —— 4/12 个有
- `Fast Bypasser (rgthree)` —— 3/12 个有
- `CR Text Replace` —— 2/12 个有
- `Note Plus (mtb)` —— 2/12 个有
- `PainterI2V` —— 2/12 个有
- `ShowText|pysssss` —— 2/12 个有
- `easy anythingIndexSwitch` —— 2/12 个有
- `AILab_QwenVL` —— 1/12 个有
- `JjkText` —— 1/12 个有
- `PreviewAny` —— 1/12 个有
- `PrimitiveBoolean` —— 1/12 个有
- `RH_Captioner` —— 1/12 个有
- `RH_Captioner_Pro` —— 1/12 个有
- `TextBox` —— 1/12 个有
- `easy convertAnything` —— 1/12 个有
- `easy ifElse` —— 1/12 个有
- `孤海注释` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 12 | 100% |
| Prompt 约束强度(CFG) | 5.5 | 5 - 6 | 12 | 91% |
| 采样算法 | 1 | 1 - 1 | 12 | 100% |
| 调度器 | 1 | 1 - 1 | 6 | 100% |
| 重绘幅度 | simple | - | 12 | 50% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，12 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 5.5，观测区间 5 - 6，12 个样本，取值集中（一致性 91%）
- 采样算法 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 调度器 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 重绘幅度 最常用 simple，12 个样本，一致性 50%
