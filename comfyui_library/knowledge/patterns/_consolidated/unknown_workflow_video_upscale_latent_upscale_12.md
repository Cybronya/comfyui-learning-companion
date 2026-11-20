---
name: unknown_workflow_video_upscale_latent_upscale_12
type: Unknown Workflow
frequency: 17
level: moderate
coverage: 0.769706
common_nodes: [BasicGuider, BasicScheduler, BlockSparseAttention, CLIPLoader, ComfyMathExpression, ExtendIntermediateSigmas, GoohaiUniversalSlider, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoraLoaderModelOnly, MinimaxH3LatentUpscaler3D, ModelAttentionBackend, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SplitSigmas, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, easy float]
problems: []
missing: []
members: [图片生成/图生图/万象AI+Singularity竖屏12秒长视频，GIMM补帧消除卡顿感_2116719321073410049.json, 图片生成/图生图/上传带人声口播视频驱动数字人，好物带货长视频直出_2116750436517634049.json, 图片生成/图生图/上传带人声口播视频驱动数字人，探店种草长视频直出_2117112915131199490.json, 图片生成/图生图/上传带人声口播视频驱动数字人，旅游种草长视频直出_2117111433929510914.json, 图片生成/图生图/上传带人声口播视频驱动数字人，知识分享长视频直出_2116751925290037249.json, 平台全量/Minimax H3_三采_捕获帧_视频无缝续接 (音频驱动)_2119633976901070849.json, 平台全量/Minimax H3_三采最强工作流_基础版_2120321445367734273.json, 平台全量/一段口播视频驱动AI数字人，好物开箱测评长视频直出_2117485266956017666.json, 平台全量/一段口播视频驱动AI数字人，居家健身教学长视频直出_2117483761146359810.json, 平台全量/一段口播视频驱动AI数字人，情感电台长视频直出_2117974877750784002.json, 视频生成/图生视频/Minimax H3_三采最强工作流_视频无缝续接_2113816891000188929.json, 视频生成/图生视频/Minimax H3_三采最强工作流_视频无缝续接_2115026605482532865.json, 视频生成/图生视频/Minimax H3_三采最强工作流_视频无缝续接_2115053303619997698.json, 视频生成/图生视频/Minimax H3_三采最强工作流_音频驱动_2113272320948260865.json, 视频生成/图生视频/Minimax H3_三采最强工作流_首尾帧_2114707872927014914.json, 视频生成/图生视频/Minimax_H3_三采最强工作流_首尾帧_2116026048046518273.json, 视频生成/图生视频/Minimax_H3_三采最强工作流_首尾帧_2116034641181368321.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_12

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（图片生成/图生图/万象AI+Singularity竖屏12秒长视频，GIMM补帧消除卡顿感_2116719321073410049.json、图片生成/图生图/上传带人声口播视频驱动数字人，好物带货长视频直出_2116750436517634049.json、图片生成/图生图/上传带人声口播视频驱动数字人，探店种草长视频直出_2117112915131199490.json、图片生成/图生图/上传带人声口播视频驱动数字人，旅游种草长视频直出_2117111433929510914.json、图片生成/图生图/上传带人声口播视频驱动数字人，知识分享长视频直出_2116751925290037249.json…）

- **类型**：Unknown Workflow
- **样本数**：17
- **可信度**：中等可信
- **平均知识覆盖**：77%

## 共有节点

全部 17 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `BlockSparseAttention`
- `CLIPLoader`
- `ComfyMathExpression`
- `ExtendIntermediateSigmas`
- `GoohaiUniversalSlider`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoraLoaderModelOnly`
- `MinimaxH3LatentUpscaler3D`
- `ModelAttentionBackend`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SplitSigmas`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `easy float`

**可变部分**（部分 workflow 才有）：
- `VAEDecodeAudio` —— 16/17 个有
- `LoadVideoUI` —— 14/17 个有
- `MiniMaxH3ReferenceToVideo` —— 14/17 个有
- `GetNode` —— 13/17 个有
- `SetNode` —— 13/17 个有
- `DisableNoise` —— 9/17 个有
- `ImageScaleToTotalPixels` —— 9/17 个有
- `LoadImage` —— 9/17 个有
- `MiniMaxH3SigmaShift` —— 9/17 个有
- `ModelPreviewOverrideKJ` —— 9/17 个有
- `忽略多组孤海` —— 9/17 个有
- `SaveImage` —— 8/17 个有
- `孤海注释` —— 8/17 个有
- `MiniMaxH3MotionContext` —— 7/17 个有
- `PreviewAny` —— 6/17 个有
- `LoadAudioUI` —— 5/17 个有
- `RH_LLMAPI_NODE` —— 5/17 个有
- `MiniMaxH3MotionContextTrim` —— 4/17 个有
- `CR Text` —— 3/17 个有
- `ImageFromBatch` —— 3/17 个有
- `MiniMaxH3AddGuide` —— 3/17 个有
- `MiniMaxH3ImageToVideo` —— 3/17 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 2/17 个有
- `DownloadAndLoadGIMMVFIModel` —— 1/17 个有
- `GIMMVFI_interpolate` —— 1/17 个有
- `PrimitiveInt` —— 1/17 个有
- `YusuLoadAudioUI` —— 1/17 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
