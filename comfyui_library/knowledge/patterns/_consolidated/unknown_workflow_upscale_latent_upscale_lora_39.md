---
name: unknown_workflow_upscale_latent_upscale_lora_39
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.596
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, H3LatentUpscaleByJingchen573, H3SigmaRefiner, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoadAudio, LoadImage, LoraLoaderModelOnly, MiniMaxH3BlockCacheT8, MiniMaxH3ReferenceToVideo, MinimaxH3LatentUpscaler3D, PathchSageAttentionKJ, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_LoadVideo, easy cleanGpuUsed]
problems: []
missing: []
members: [图片生成/图生图/MiniMax_H3_电影质感正式版_2100140264701648898.json, 视频生成/图生视频/MiniMax H3全能参考+Latent放大 ｜真实电影质感_2097236111977439233.json, 视频生成/图生视频/MiniMax_H3_电影质感正式版_2100061128037588994.json, 视频生成/文生视频/MiniMax H3 真实电影质感【无水印正式版】｜全能参考｜Latent放大_2108365559254568962.json, 视频生成/文生视频/MiniMax H3 真实电影质感【正式版】｜全能参考+Latent放大_2099642261834391553.json, 视频生成/文生视频/MiniMax H3 真实电影质感｜全能参考+Latent放大_2094202685590429698.json, 视频生成/文生视频/MiniMax H3_电影质感正式版_2092438021516906497.json, 视频生成/文生视频/MiniMax_H3远景模糊人脸修复_2100874075915767810.json, 视频生成/视频生视频/MiniMax H3_电影质感正式版_2105690903259209729.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_39

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/MiniMax_H3_电影质感正式版_2100140264701648898.json、视频生成/图生视频/MiniMax H3全能参考+Latent放大 ｜真实电影质感_2097236111977439233.json、视频生成/图生视频/MiniMax_H3_电影质感正式版_2100061128037588994.json、视频生成/文生视频/MiniMax H3 真实电影质感【无水印正式版】｜全能参考｜Latent放大_2108365559254568962.json、视频生成/文生视频/MiniMax H3 真实电影质感【正式版】｜全能参考+Latent放大_2099642261834391553.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：60%

## 共有节点

全部 9 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `H3LatentUpscaleByJingchen573`
- `H3SigmaRefiner`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3BlockCacheT8`
- `MiniMaxH3ReferenceToVideo`
- `MinimaxH3LatentUpscaler3D`
- `PathchSageAttentionKJ`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_LoadVideo`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 8/9 个有
- `DisableNoise` —— 8/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 8/9 个有
- `SaveVideo` —— 8/9 个有
- `SplitSigmas` —— 8/9 个有
- `easy anythingIndexSwitch` —— 7/9 个有
- `GetNode` —— 5/9 个有
- `MiniMaxH3ImageToVideo` —— 5/9 个有
- `SetNode` —— 5/9 个有
- `Any Switch (rgthree)` —— 4/9 个有
- `Fast Groups Muter (rgthree)` —— 4/9 个有
- `FastGroupsBypassSwitch` —— 4/9 个有
- `MuyeTextEditOutput` —— 4/9 个有
- `PrimitiveInt` —— 4/9 个有
- `ShowText|pysssss` —— 4/9 个有
- `CR Text Concatenate` —— 3/9 个有
- `Fast Groups Bypasser (rgthree)` —— 3/9 个有
- `孤海注释` —— 3/9 个有
- `H3FaceStitch` —— 1/9 个有
- `H3FaceTrackCrop` —— 1/9 个有
- `H3InjectVideoLatent` —— 1/9 个有
- `H3PerFrameDenoise` —— 1/9 个有
- `MiniMaxH3NativeAudioLock` —— 1/9 个有
- `MmuuaiGroupBypass` —— 1/9 个有
- `VHS_VideoCombine` —— 1/9 个有
- `easy showAnything` —— 1/9 个有
- `忽略多组孤海` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
