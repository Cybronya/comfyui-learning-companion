---
name: unknown_workflow_video_lora_clip_5
type: Unknown Workflow
frequency: 15
level: strong
coverage: 0.825733
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, ImpactInt, LoadImage, LoraLoaderModelOnly, MathExpression|pysssss, ModelPatchTorchSettings, ModelSamplingSD3, Mute / Bypass Repeater (rgthree), PathchSageAttentionKJ, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/WH-AI-Studio-Wan2.2-运镜加速完美版-图生视频_2015621082249695233.json, 视频生成/图生视频/Wan2.2-Remix-V2最好用的图生视频_2044778241440878594.json, 视频生成/图生视频/Wan2.2-RemixV2-i2V首-中-尾三帧图生视频（补帧版）_2004448148036743169.json, 视频生成/图生视频/Wan2.2-RemixV2_首-中-尾图生视频（补帧版）_2044949937833648130.json, 视频生成/图生视频/Wan2.2图生视频 超写实 提示词全自动生成_1998067601303592962.json, 视频生成/图生视频/wan2.2急速 图生视频，高度准确，可本地运行_2048957186650411010.json, 视频生成/图生视频/wan2.2急速 图生视频，高度准确，可本地运行_2048963923868651521.json, 视频生成/图生视频/全能视频V3图生视频 超写实 提示词全自动生成_2003494733840326657.json, 视频生成/图生视频/图片+文字描述反推视频V2_2004485474582491138.json, 视频生成/图生视频/图生视频_1999866584787189761.json, 视频生成/图生视频/图生视频修改_2009703059848433666.json, 视频生成/图生视频/自己用：WAN2.2 首-中-尾三帧视频_1995871221013176322.json, 视频生成/图生视频/视频首尾帧_1999869962674204673.json, 视频生成/图生视频/🕵🏻大丝袜 动漫专属模型 Dasiwa 图生视频🕵🏻_2007995692123426818.json, 视频生成/图生视频/🕵🏻大丝袜 动漫专属模型 Dasiwa 首尾帧视频🕵🏻_2008006375305125889.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_clip_5

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（视频生成/图生视频/WH-AI-Studio-Wan2.2-运镜加速完美版-图生视频_2015621082249695233.json、视频生成/图生视频/Wan2.2-Remix-V2最好用的图生视频_2044778241440878594.json、视频生成/图生视频/Wan2.2-RemixV2-i2V首-中-尾三帧图生视频（补帧版）_2004448148036743169.json、视频生成/图生视频/Wan2.2-RemixV2_首-中-尾图生视频（补帧版）_2044949937833648130.json、视频生成/图生视频/Wan2.2图生视频 超写实 提示词全自动生成_1998067601303592962.json…）

- **类型**：Unknown Workflow
- **样本数**：15
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 15 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `ImpactInt`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MathExpression|pysssss`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `Mute / Bypass Repeater (rgthree)`
- `PathchSageAttentionKJ`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 14/15 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 14/15 个有
- `RIFE VFI` —— 14/15 个有
- `SetNode` —— 14/15 个有
- `easy getNode` —— 14/15 个有
- `easy setNode` —— 14/15 个有
- `CR Text` —— 13/15 个有
- `wanBlockSwap` —— 13/15 个有
- `Fast Muter (rgthree)` —— 10/15 个有
- `WanMoeKSampler` —— 9/15 个有
- `ImageResizeKJ` —— 8/15 个有
- `PainterI2V` —— 7/15 个有
- `KSamplerAdvanced` —— 6/15 个有
- `WanFirstMiddleLastFrameToVideo` —— 6/15 个有
- `Fast Bypasser (rgthree)` —— 5/15 个有
- `ShowText|pysssss` —— 3/15 个有
- `Note Plus (mtb)` —— 2/15 个有
- `WanFirstLastFrameToVideo` —— 2/15 个有
- `easy anythingIndexSwitch` —— 2/15 个有
- `CR Text Replace` —— 1/15 个有
- `ImageResizeKJv2` —— 1/15 个有
- `Int` —— 1/15 个有
- `LayerUtility: PurgeVRAM` —— 1/15 个有
- `RH_Captioner` —— 1/15 个有
- `RH_Captioner_Pro` —— 1/15 个有
- `RH_LLMAPI_NODE` —— 1/15 个有
- `TTResolutionSelector` —— 1/15 个有
- `easy cleanGpuUsed` —— 1/15 个有
- `easy convertAnything` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 15 | 100% |
| Prompt 约束强度(CFG) | 6 | 5 - 6 | 15 | 91% |
| 采样算法 | 1 | 1 - 1 | 15 | 100% |
| 调度器 | 1 | 1 - 1 | 9 | 100% |
| 重绘幅度 | euler_ancestral | - | 15 | 60% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，15 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 6，观测区间 5 - 6，15 个样本，取值集中（一致性 91%）
- 采样算法 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 调度器 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 重绘幅度 最常用 euler_ancestral，15 个样本，一致性 60%
