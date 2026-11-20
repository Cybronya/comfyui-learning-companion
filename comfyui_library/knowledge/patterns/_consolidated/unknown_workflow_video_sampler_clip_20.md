---
name: unknown_workflow_video_sampler_clip_20
type: Unknown Workflow
frequency: 20
level: strong
coverage: 0.77585
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CR Text, JWInteger, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, MathExpression|pysssss, ModelSamplingSD3, PathchSageAttentionKJ, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, easy showAnything, wanBlockSwap]
problems: []
missing: []
members: [图片生成/图生图/RemixV2首尾帧视频更强动态_2024095480057176066.json, 图片生成/图生图/Wan2.2双模型首尾帧视频 (1)_2085273690295590914.json, 视频生成/图生视频/RemixV2首尾帧视频更强动态_1988081469920882689.json, 视频生成/图生视频/RemixV2首尾帧视频更强动态_1988165926900121601.json, 视频生成/图生视频/WAN2.2-LightX2V-I2V高动态首尾帧_1980947136646959105.json, 视频生成/图生视频/Wan2.2 Smooth Mix 生成首尾帧视频_1979748549997006850.json, 视频生成/图生视频/Wan2.2 Smooth Mix图生视频（高动态）_1979541039348355074.json, 视频生成/图生视频/Wan2.2 Smooth Mix首尾帧视频（高动态）_1979545928719831042.json, 视频生成/图生视频/Wan2.2 Smooth Mix首尾帧视频（高动态）_2017190232734568450.json, 视频生成/图生视频/Wan2.2 Smooth Mix高动态图生视频V1_1979756399754383362.json, 视频生成/图生视频/Wan2.2 Smooth Mix高动态首尾帧V1_1979756565743964162.json, 视频生成/图生视频/Wan2.2+新版lightx2v加速-4步图生视频【官版】_1950101403698159617.json, 视频生成/图生视频/Wan2.2-DaSiWa-最强动漫模型-首尾帧视频-插帧放大-自动提示词_2010927245770100738.json, 视频生成/图生视频/Wan2.2动漫模型DaSiWa-首尾帧视频_2013598944579821569.json, 视频生成/图生视频/Wan2.2动漫模型DaSiWa-首尾帧视频_2076910094813589506.json, 视频生成/图生视频/【首尾帧】Wan2.2 Smooth Mix 图生视频 高动态_1979745226703147009.json, 视频生成/图生视频/动漫短剧图生视频动态优化工作流（lora版+自动提示词）_1982328615742382081.json, 视频生成/图生视频/动漫转真人最强首尾帧控制_2013169073936408577.json, 视频生成/图生视频/王中王首尾帧微型--吊打闭源【万物生长 2】_1980857970835804161.json, 视频生成/图生视频/王炸首尾帧--吊打闭源【万物生长 】_1980631743067803649.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_20

> 由 `engine/knowledge_consolidation` 从 20 个 workflow 归纳得出（图片生成/图生图/RemixV2首尾帧视频更强动态_2024095480057176066.json、图片生成/图生图/Wan2.2双模型首尾帧视频 (1)_2085273690295590914.json、视频生成/图生视频/RemixV2首尾帧视频更强动态_1988081469920882689.json、视频生成/图生视频/RemixV2首尾帧视频更强动态_1988165926900121601.json、视频生成/图生视频/WAN2.2-LightX2V-I2V高动态首尾帧_1980947136646959105.json…）

- **类型**：Unknown Workflow
- **样本数**：20
- **可信度**：强结论
- **平均知识覆盖**：78%

## 共有节点

全部 20 个 workflow 都包含：
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
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `easy showAnything`
- `wanBlockSwap`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 19/20 个有
- `ModelPatchTorchSettings` —— 19/20 个有
- `RH_LLMAPI_NODE` —— 19/20 个有
- `SetNode` —— 19/20 个有
- `Fast Groups Bypasser (rgthree)` —— 16/20 个有
- `ImageConcanate` —— 16/20 个有
- `ImageResizeKJ` —— 16/20 个有
- `RIFE VFI` —— 16/20 个有
- `WanFirstLastFrameToVideo` —— 16/20 个有
- `ImpactSwitch` —— 15/20 个有
- `SeedVR2BlockSwap` —— 15/20 个有
- `SeedVR2ExtraArgs` —— 15/20 个有
- `SeedVR2GGUF` —— 15/20 个有
- `LoraLoaderModelOnly` —— 6/20 个有
- `ShowText|pysssss` —— 6/20 个有
- `easy textSwitch` —— 5/20 个有
- `Text Concatenate` —— 4/20 个有
- `Wan22PromptSelector` —— 4/20 个有
- `WanImageToVideo` —— 4/20 个有
- `PreviewImage` —— 3/20 个有
- `SaveImage` —— 3/20 个有
- `PromptTemplateSelector` —— 2/20 个有
- `RH_Nano_Banana_Image2Image` —— 2/20 个有
- `AddLabel` —— 1/20 个有
- `GetImageSizeAndCount` —— 1/20 个有
- `Images to RGB` —— 1/20 个有
- `Int` —— 1/20 个有
- `Make Image Grid JK` —— 1/20 个有
- `Qwen3_VQA` —— 1/20 个有
- `TT_img_enc` —— 1/20 个有
- `intToFloat _O` —— 1/20 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 20 | 95% |
| Prompt 约束强度(CFG) | 6 | 4 - 6 | 20 | 93% |
| 采样算法 | 1 | 1 - 1 | 20 | 100% |
| 调度器 | euler_ancestral | - | 20 | 70% |
| 重绘幅度 | simple | - | 20 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，20 个样本，一致性 95%
- Prompt 约束强度(CFG) 中位数 6，观测区间 4 - 6，20 个样本，取值集中（一致性 93%）
- 采样算法 中位数 1，观测区间 1 - 1，20 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler_ancestral，20 个样本，一致性 70%
- 重绘幅度 最常用 simple，20 个样本，一致性 100%
