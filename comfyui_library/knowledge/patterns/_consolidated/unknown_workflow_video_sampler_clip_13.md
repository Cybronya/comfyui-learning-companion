---
name: unknown_workflow_video_sampler_clip_13
type: Unknown Workflow
frequency: 24
level: strong
coverage: 0.833
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text, JWInteger, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, MathExpression|pysssss, ModelPatchTorchSettings, ModelSamplingSD3, PathchSageAttentionKJ, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/RemixV2首尾帧视频更强动态_2024095480057176066.json, 图片生成/图生图/Wan2.2双模型首尾帧视频 (1)_2085273690295590914.json, 视频生成/图生视频/Remix-Wan2.2 首尾帧 高动态画质_1987535452620173313.json, 视频生成/图生视频/RemixV2首尾帧视频更强动态_1988081469920882689.json, 视频生成/图生视频/RemixV2首尾帧视频更强动态_1988165926900121601.json, 视频生成/图生视频/WAN2.2-LightX2V-I2V高动态首尾帧_1980947136646959105.json, 视频生成/图生视频/Wan2.2 Smooth Mix 生成首尾帧视频_1979748549997006850.json, 视频生成/图生视频/Wan2.2 Smooth Mix首尾帧视频（高动态）_1979545928719831042.json, 视频生成/图生视频/Wan2.2 Smooth Mix首尾帧视频（高动态）_2017190232734568450.json, 视频生成/图生视频/Wan2.2 Smooth Mix高动态首尾帧V1_1979756565743964162.json, 视频生成/图生视频/Wan2.2-DaSiWa-最强动漫模型-首尾帧视频-插帧放大-自动提示词_2010927245770100738.json, 视频生成/图生视频/Wan2.2-remix+VQA 首尾帧_1988124359338389506.json, 视频生成/图生视频/Wan2.2动漫模型DaSiWa-首尾帧视频_2013598944579821569.json, 视频生成/图生视频/Wan2.2动漫模型DaSiWa-首尾帧视频_2076910094813589506.json, 视频生成/图生视频/Wan2.2双模型首尾帧图生视频_2080624345147334658.json, 视频生成/图生视频/Wan2.2双模型首尾帧视频_2082282165500469249.json, 视频生成/图生视频/Wan2.2双模型首尾帧视频_2083014224594427906.json, 视频生成/图生视频/Wan2.2双模型首尾帧视频_2083105850020950017.json, 视频生成/图生视频/Wan_2.2_FMLF多帧首尾帧_2067206177418727425.json, 视频生成/图生视频/Wan_2.2_FMLF多帧首尾帧视频_1988612935910121474.json, 视频生成/图生视频/【首尾帧】Wan2.2 Smooth Mix 图生视频 高动态_1979745226703147009.json, 视频生成/图生视频/动漫转真人最强首尾帧控制_2013169073936408577.json, 视频生成/图生视频/嘟嘟-Wan_2.2_FMLF多帧首尾帧_1988086364040310785.json, 视频生成/图生视频/首尾帧 Wan2.2-Remix 高动态，高画质_1987524619294978050.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_13

> 由 `engine/knowledge_consolidation` 从 24 个 workflow 归纳得出（图片生成/图生图/RemixV2首尾帧视频更强动态_2024095480057176066.json、图片生成/图生图/Wan2.2双模型首尾帧视频 (1)_2085273690295590914.json、视频生成/图生视频/Remix-Wan2.2 首尾帧 高动态画质_1987535452620173313.json、视频生成/图生视频/RemixV2首尾帧视频更强动态_1988081469920882689.json、视频生成/图生视频/RemixV2首尾帧视频更强动态_1988165926900121601.json…）

- **类型**：Unknown Workflow
- **样本数**：24
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 24 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `JWInteger`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `MathExpression|pysssss`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `wanBlockSwap` —— 23/24 个有
- `CLIPVisionEncode` —— 21/24 个有
- `CLIPVisionLoader` —— 21/24 个有
- `ImageConcanate` —— 21/24 个有
- `ImageResizeKJ` —— 21/24 个有
- `WanFirstLastFrameToVideo` —— 21/24 个有
- `SetNode` —— 19/24 个有
- `Fast Groups Bypasser (rgthree)` —— 18/24 个有
- `GetNode` —— 18/24 个有
- `RIFE VFI` —— 17/24 个有
- `SeedVR2BlockSwap` —— 17/24 个有
- `SeedVR2ExtraArgs` —— 17/24 个有
- `SeedVR2GGUF` —— 17/24 个有
- `RH_LLMAPI_NODE` —— 16/24 个有
- `ImpactSwitch` —— 14/24 个有
- `LoraLoaderModelOnly` —— 10/24 个有
- `easy textSwitch` —— 10/24 个有
- `ImageConcatMulti` —— 6/24 个有
- `Images to RGB` —— 5/24 个有
- `Qwen3_VQA` —— 5/24 个有
- `intToFloat _O` —— 5/24 个有
- `PreviewImage` —— 4/24 个有
- `ImageBatchMulti` —— 3/24 个有
- `ImageScaleToTotalPixels` —— 3/24 个有
- `LayerUtility: PurgeVRAM V2` —— 3/24 个有
- `WanFirstMiddleLastFrameToVideo` —— 3/24 个有
- `WanMultiFrameRefToVideo` —— 3/24 个有
- `RHHiddenNodes` —— 2/24 个有
- `AddLabel` —— 1/24 个有
- `Int` —— 1/24 个有
- `Make Image Grid JK` —— 1/24 个有
- `Qwen3_VQA_Plus` —— 1/24 个有
- `SaveImage` —— 1/24 个有
- `TT_img_enc` —— 1/24 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 24 | 88% |
| Prompt 约束强度(CFG) | 6 | 6 - 6 | 24 | 100% |
| 采样算法 | 1 | 1 - 1 | 24 | 100% |
| 调度器 | euler_ancestral | - | 24 | 62% |
| 重绘幅度 | simple | - | 24 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，24 个样本，一致性 88%
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 6，24 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，24 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler_ancestral，24 个样本，一致性 62%
- 重绘幅度 最常用 simple，24 个样本，一致性 100%
