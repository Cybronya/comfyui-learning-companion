---
name: text_to_image_lora_sampler_clip_98
type: Text To Image
frequency: 11
level: strong
coverage: 0.892091
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, CreateVideo, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoraLoaderModelOnly, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/文生图一次15图｜MiniMaxH3爆图工作流批量生成_2093721661387395074.json, 视频生成/文生视频/8步加速文生视频｜minimax_h3文字生成视频工作流_2088367583484538882.json, 视频生成/文生视频/DiT int8加速｜MiniMax H3 FL2VA开源版图像音频参考生视频_2090821057673519105.json, 视频生成/文生视频/FL2VA首尾帧文生全能｜MiniMax H3视频生成工作流_2093069819640901634.json, 视频生成/文生视频/H3真实电影质感正式版 全能参考Latent放大_2099956140791656450.json, 视频生成/文生视频/MiniMax H3 FL2VA文生首尾帧全能视频｜文生视频视频生视频图生视频_2090423722896347138.json, 视频生成/文生视频/MiniMax H3 latent放大双采+8步lora｜全能参考顶级质速_2089440965449834498.json, 视频生成/文生视频/MiniMax H3全能参考｜latent放大双采+8步lora质量速度兼得_2089466163435761666.json, 视频生成/文生视频/MiniMax H3真实电影质感｜高质量视频生成_2095284422009507842.json, 视频生成/文生视频/MiniMax H3远景模糊人脸修复视频生成处理工具_2101368651281682433.json, 视频生成/文生视频/远景模糊人脸修复利器｜MiniMax_H3视频增强_2101179629947146242.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_98

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/文生图一次15图｜MiniMaxH3爆图工作流批量生成_2093721661387395074.json、视频生成/文生视频/8步加速文生视频｜minimax_h3文字生成视频工作流_2088367583484538882.json、视频生成/文生视频/DiT int8加速｜MiniMax H3 FL2VA开源版图像音频参考生视频_2090821057673519105.json、视频生成/文生视频/FL2VA首尾帧文生全能｜MiniMax H3视频生成工作流_2093069819640901634.json、视频生成/文生视频/H3真实电影质感正式版 全能参考Latent放大_2099956140791656450.json…）

- **类型**：Text To Image
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 11 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `CreateVideo`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `PrimitiveFloat` —— 10/11 个有
- `VAEDecodeAudio` —— 10/11 个有
- `LTXVConcatAVLatent` —— 9/11 个有
- `LTXVSeparateAVLatent` —— 9/11 个有
- `LoadImage` —— 9/11 个有
- `PrimitiveStringMultiline` —— 9/11 个有
- `MiniMaxH3ImageToVideo` —— 8/11 个有
- `PathchSageAttentionKJ` —— 7/11 个有
- `SplitSigmas` —— 7/11 个有
- `H3LatentUpscaleByJingchen573` —— 6/11 个有
- `H3SigmaRefiner` —— 6/11 个有
- `LoadAudio` —— 6/11 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 6/11 个有
- `MiniMaxH3ReferenceToVideo` —— 6/11 个有
- `MinimaxH3LatentUpscaler3D` —— 6/11 个有
- `easy showAnything` —— 6/11 个有
- `easy cleanGpuUsed` —— 5/11 个有
- `DisableNoise` —— 4/11 个有
- `MiniMaxH3BlockCacheT8` —— 4/11 个有
- `ShowText|pysssss` —— 4/11 个有
- `VHS_LoadVideo` —— 4/11 个有
- `Fast Groups Bypasser (rgthree)` —— 3/11 个有
- `SaveImage` —— 3/11 个有
- `easy anythingIndexSwitch` —— 3/11 个有
- `H3FaceStitch` —— 2/11 个有
- `H3FaceTrackCrop` —— 2/11 个有
- `H3InjectVideoLatent` —— 2/11 个有
- `H3PerFrameDenoise` —— 2/11 个有
- `LatentUpscaleBy` —— 2/11 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/11 个有
- `MiniMaxH3HybridLoader` —— 2/11 个有
- `MiniMaxH3NativeAudioLock` —— 2/11 个有
- `MiniMaxH3SigmaShift` —— 2/11 个有
- `ModelPatchTorchSettings` —— 2/11 个有
- `ModelPreviewOverrideKJ` —— 2/11 个有
- `MuyeTextEditOutput` —— 2/11 个有
- `PrimitiveInt` —— 2/11 个有
- `Any Switch (rgthree)` —— 1/11 个有
- `ExtractStoryboards_xuhuan1024` —— 1/11 个有
- `Int` —— 1/11 个有
- `MinimaxH3LatentUpscalerNode3D` —— 1/11 个有
- `RH_LLMAPI_Pro_Node` —— 1/11 个有
- `Text` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 11 | 100% |
| 高度 | 80 | 80 - 80 | 11 | 100% |
| 采样步数 | 4 | 4 - 4 | 11 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 11 | 100% |
| 采样算法 | er_sde | - | 11 | 100% |
| 调度器 | beta | - | 11 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 12/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，11 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，11 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，11 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，11 个样本，一致性 100%
- 调度器 最常用 beta，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 高发问题（12/11 个样本）：Steps较低可能导致细节不足
