---
name: text_to_image_lora_sampler_clip_52
type: Text To Image
frequency: 17
level: strong
coverage: 0.899824
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/v2.0多参双采样图影音｜minimax h3电影感大片生成_2094317653564420098.json, 视频生成/图生视频/一键换脸生成新人物｜MiniMax H3角色替换图生视频 视频生视频_2090814396544151553.json, 视频生成/图生视频/三图multi_ref参考生成｜minimax h3 i2v视频_2094928789578014722.json, 视频生成/图生视频/三图参考生视频｜multi_ref_minimax_h3_i2v生成_2095108277595099138.json, 视频生成/图生视频/去除ai感全能参考｜minimax h3转场运镜图生视频_2093435277451812865.json, 视频生成/图生视频/去除ai感转场运镜｜minimax h3全能参考图生视频_2093764750915231745.json, 视频生成/图生视频/图像+视频+音频参考｜H3生成视频多模态工作流_2094735141095694338.json, 视频生成/图生视频/多参双采样图影音电影感大片 minimax h3 v2.0视频制作_2094183296849768450.json, 视频生成/图生视频/极致电影质感｜Minimax-H3转场运镜图生视频_2093229463424299009.json, 视频生成/图生视频/电影级视频多参版v1.0｜minimax H3制作工作流_2093475759825440770.json, 视频生成/图生视频/电影质感极致呈现｜Minimax-H3运镜转场图生视频_2093071322497769473.json, 视频生成/文生视频/8步加速电影质感 Minimax H3 文生视频LoRA强化出片_2094165667820957697.json, 视频生成/文生视频/H3真实电影质感全能参考 文生视频图生视频_2100309862587654145.json, 视频生成/文生视频/H3真实电影质感正式版 全能参考Latent放大_2099956140791656450.json, 视频生成/文生视频/MiniMax H3真实电影质感｜高质量视频生成_2095284422009507842.json, 视频生成/文生视频/MiniMax H3远景模糊人脸修复视频生成处理工具_2101368651281682433.json, 视频生成/文生视频/远景模糊人脸修复利器｜MiniMax_H3视频增强_2101179629947146242.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_52

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（视频生成/图生视频/v2.0多参双采样图影音｜minimax h3电影感大片生成_2094317653564420098.json、视频生成/图生视频/一键换脸生成新人物｜MiniMax H3角色替换图生视频 视频生视频_2090814396544151553.json、视频生成/图生视频/三图multi_ref参考生成｜minimax h3 i2v视频_2094928789578014722.json、视频生成/图生视频/三图参考生视频｜multi_ref_minimax_h3_i2v生成_2095108277595099138.json、视频生成/图生视频/去除ai感全能参考｜minimax h3转场运镜图生视频_2093435277451812865.json…）

- **类型**：Text To Image
- **样本数**：17
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 17 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `PathchSageAttentionKJ` —— 16/17 个有
- `PrimitiveStringMultiline` —— 16/17 个有
- `VAEDecodeAudio` —— 16/17 个有
- `LoadAudio` —— 15/17 个有
- `VHS_LoadVideo` —— 15/17 个有
- `CreateVideo` —— 13/17 个有
- `MiniMaxH3BlockCacheT8` —— 13/17 个有
- `SaveVideo` —— 13/17 个有
- `easy anythingIndexSwitch` —— 12/17 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 11/17 个有
- `Fast Groups Bypasser (rgthree)` —— 7/17 个有
- `H3SigmaRefiner` —— 7/17 个有
- `MiniMaxH3ImageToVideo` —— 7/17 个有
- `easy showAnything` —— 7/17 个有
- `DisableNoise` —— 5/17 个有
- `SaveImage` —— 5/17 个有
- `SplitSigmas` —— 5/17 个有
- `H3LatentUpscaleByJingchen573` —— 4/17 个有
- `LTXVConcatAVLatent` —— 4/17 个有
- `LTXVSeparateAVLatent` —— 4/17 个有
- `LoraLoaderBypassModelOnly` —— 4/17 个有
- `MinimaxH3LatentUpscaler3D` —— 4/17 个有
- `VHS_VideoCombine` —— 4/17 个有
- `easy cleanGpuUsed` —— 4/17 个有
- `PainterVRAM` —— 3/17 个有
- `FlashVSRNode` —— 2/17 个有
- `H3FaceStitch` —— 2/17 个有
- `H3FaceTrackCrop` —— 2/17 个有
- `H3InjectVideoLatent` —— 2/17 个有
- `H3PerFrameDenoise` —— 2/17 个有
- `MiniMaxH3NativeAudioLock` —— 2/17 个有
- `MuyeTextEditOutput` —— 2/17 个有
- `ShowText|pysssss` —— 2/17 个有
- `Sleep` —— 2/17 个有
- `YK_LoadImageFromURL` —— 2/17 个有
- `Any Switch (rgthree)` —— 1/17 个有
- `Int` —— 1/17 个有
- `Text` —— 1/17 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 17 | 100% |
| 高度 | 80 | 80 - 80 | 17 | 100% |
| 采样步数 | 4 | 4 - 4 | 17 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 17 | 100% |
| 采样算法 | er_sde | - | 17 | 100% |
| 调度器 | beta | - | 17 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 17 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 17/17 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，17 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，17 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，17 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，17 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，17 个样本，一致性 100%
- 调度器 最常用 beta，17 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，17 个样本，取值集中（一致性 100%）
- 高发问题（17/17 个样本）：Steps较低可能导致细节不足
