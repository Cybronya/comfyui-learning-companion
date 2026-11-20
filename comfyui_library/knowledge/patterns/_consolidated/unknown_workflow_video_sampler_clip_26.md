---
name: unknown_workflow_video_sampler_clip_26
type: Unknown Workflow
frequency: 16
level: strong
coverage: 0.822875
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CR Text, JWInteger, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, MathExpression|pysssss, ModelPatchTorchSettings, ModelSamplingSD3, PathchSageAttentionKJ, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/RemixV2首尾帧视频更强动态_2024095480057176066.json, 图片生成/图生图/Wan2.2双模型首尾帧视频 (1)_2085273690295590914.json, 平台全量/wan2.2 DaSiWa-首尾帧视频_2009443551440019457.json, 数字人/数字人/二维漫画风格 Wan2.2-Dasiwa_2005829347586048001.json, 视频生成/图生视频/Remix-Wan2.2 首尾帧 高动态画质_1987535452620173313.json, 视频生成/图生视频/RemixV2首尾帧视频更强动态_1988081469920882689.json, 视频生成/图生视频/RemixV2首尾帧视频更强动态_1988165926900121601.json, 视频生成/图生视频/Wan2.2 Smooth Mix 生成首尾帧视频_1979748549997006850.json, 视频生成/图生视频/Wan2.2-Dasiwa 二次元动漫_1990436662905901058.json, 视频生成/图生视频/Wan2.2-remix+VQA 首尾帧_1988124359338389506.json, 视频生成/图生视频/【首尾帧】Wan2.2 Smooth Mix 图生视频 高动态_1979745226703147009.json, 视频生成/图生视频/动漫转真人最强首尾帧控制_2013169073936408577.json, 视频生成/图生视频/图生视频 高画质，高动态 高遵循度 Wan2.2 Remix_1987522876448419841.json, 视频生成/图生视频/图生视频 高画质，高动态 高遵循度 Wan2.2_2025865580863037441.json, 视频生成/图生视频/图生视频工作流_2050780959615791106.json, 视频生成/图生视频/图生视频工作流_2054015321224302593.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_26

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（图片生成/图生图/RemixV2首尾帧视频更强动态_2024095480057176066.json、图片生成/图生图/Wan2.2双模型首尾帧视频 (1)_2085273690295590914.json、平台全量/wan2.2 DaSiWa-首尾帧视频_2009443551440019457.json、数字人/数字人/二维漫画风格 Wan2.2-Dasiwa_2005829347586048001.json、视频生成/图生视频/Remix-Wan2.2 首尾帧 高动态画质_1987535452620173313.json…）

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
- `Fast Groups Bypasser (rgthree)` —— 15/16 个有
- `SetNode` —— 15/16 个有
- `wanBlockSwap` —— 15/16 个有
- `GetNode` —— 14/16 个有
- `RH_LLMAPI_NODE` —— 14/16 个有
- `RIFE VFI` —— 14/16 个有
- `SeedVR2BlockSwap` —— 14/16 个有
- `SeedVR2ExtraArgs` —— 14/16 个有
- `SeedVR2GGUF` —— 14/16 个有
- `LoraLoaderModelOnly` —— 11/16 个有
- `WanFirstLastFrameToVideo` —— 10/16 个有
- `ImageConcanate` —— 8/16 个有
- `ImageResizeKJ` —— 8/16 个有
- `LayerUtility: PurgeVRAM V2` —— 8/16 个有
- `AILab_QwenVL` —— 6/16 个有
- `CR Text Input Switch (4 way)` —— 6/16 个有
- `CombinationText` —— 6/16 个有
- `WanImageToVideo` —— 6/16 个有
- `easy cleanGpuUsed` —— 6/16 个有
- `ImpactSwitch` —— 5/16 个有
- `easy textSwitch` —— 5/16 个有
- `PreviewImage` —— 3/16 个有
- `ImageConcatMulti` —— 2/16 个有
- `CompressImages` —— 1/16 个有
- `Images to RGB` —— 1/16 个有
- `Int` —— 1/16 个有
- `Make Image Grid JK` —— 1/16 个有
- `Qwen3_VQA` —— 1/16 个有
- `Qwen3_VQA_Plus` —— 1/16 个有
- `intToFloat _O` —— 1/16 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 16 | 50% |
| Prompt 约束强度(CFG) | 6 | 6 - 6 | 16 | 100% |
| 采样算法 | 1 | 1 - 1 | 16 | 100% |
| 调度器 | euler_ancestral | - | 16 | 81% |
| 重绘幅度 | simple | - | 16 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，16 个样本，一致性 50%
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 6，16 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，16 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler_ancestral，16 个样本，一致性 81%
- 重绘幅度 最常用 simple，16 个样本，一致性 100%
