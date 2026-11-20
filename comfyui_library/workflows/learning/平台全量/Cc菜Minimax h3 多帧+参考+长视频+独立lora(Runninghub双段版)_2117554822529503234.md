---
key: 平台全量/Cc菜Minimax h3 多帧+参考+长视频+独立lora(Runninghub双段版)_2117554822529503234.json
name: Cc菜Minimax h3 多帧+参考+长视频+独立lora(Runninghub双段版)_2117554822529503234
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Cc菜Minimax h3 多帧+参考+长视频+独立lora(Runninghub双段版)_2117554822529503234.json
hash: e3d5705ea5c25630
coverage: 0.605714
learned_at: 2026-11-14 00:22:08
nodes: [SetNode, VAELoader, CLIPLoader, KSamplerSelect, SetNode, ResolutionSelector, Fast Bypasser (rgthree), LoadImage, LoadImage, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, CreateVideo, GetNode, GetNode, ComfyMathExpression, SetNode, ComfyMathExpression, GetNode, ComfyMathExpression, SetNode, Any Switch (rgthree), Any Switch (rgthree), Any Switch (rgthree), VRGDG_MiniMaxH3AudioDrive, MiniMaxH3AddGuide, GetNode, CreateVideo, SetNode, SetNode, MarkdownNote, MarkdownNote, MarkdownNote, VRGDG_MiniMaxH3AudioDrive, PrimitiveFloat, PrimitiveFloat, MiniMaxH3AddGuide, LoadImage, SaveVideo, SetNode, VAELoader, SetNode, LoadAudio, LoadImage, LoadImage, LoadImage, Fast Bypasser (rgthree), TrimAudioDuration, MiniMaxH3AddGuide, MiniMaxH3ReferenceToVideo, Reroute, MiniMaxH3AddGuide, LoadImage, LoadImage, LoadImage, MiniMaxH3ReferenceToVideo, MiniMaxH3AddGuide, BasicScheduler, VHS_LoadVideoPath, MarkdownNote, MiniMaxH3AddGuide, LoadImage, MiniMaxH3AddGuide, LoadImage, GetNode, GetNode, SetNode, GetNode, SetNode, GetNode, VHS_VideoCombine, VHS_VideoCombine, LoadImage, LoadImage, LoadImage, LoadImage, LoraLoaderModelOnly, SetNode, KSamplerSelect, SetNode, SetNode, BasicScheduler, ManualSigmas, Reroute, GetNode, ModelPreviewOverrideKJ, GetNode, GetNode, SetNode, ModelPreviewOverrideKJ, GetNode, GetNode, Reroute, Any Switch (rgthree), GetNode, GetNode, GetNode, MiniMaxH3SemanticBridgeConfigT8, MiniMaxH3SemanticBridgeApplyT8, MiniMaxH3SemanticBridgeConfigT8, MiniMaxH3SemanticBridgeApplyT8, ImageFromBatch, TrimAudioDuration, ManualSigmas, ManualSigmas, ManualSigmas, MarkdownNote, MarkdownNote, WanEx_VideoColorMatch, ManualSigmas, ManualSigmas, LoraLoaderModelOnly, 忽略多组孤海, 忽略多组孤海, 忽略多组孤海, 忽略多组孤海, 忽略多组孤海, 忽略多组孤海, 忽略多组孤海, 3000688f-5a2b-435a-9a09-b8b8cf4dfda5, TrimAudioDuration, LoadAudio, TrimAudioDuration, LoadAudio, TrimAudioDuration, LoadAudio, 忽略多组孤海, 忽略多组孤海, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, GoohaiUniversalSlider, 忽略多组孤海, 忽略多组孤海, LoraLoaderModelOnly, GoohaiUniversalSlider, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, VHS_LoadVideo, VHS_LoadVideo, VHS_LoadVideo, VHS_LoadVideo, LoraLoaderModelOnly, Fast Groups Muter (rgthree), GetNode, GetNode, 3860701b-afbc-4fc6-8627-77d475b3f0cb, Text, 216f7681-5aed-48b7-a1ca-9cdceaa9cea0, Text, b3e2b2b0-1f68-4478-ac79-5d00ccb733ae, SetNode, c92f4563-479c-4ac9-aa17-7b8843e30c35, AD_video_merge, SetNode, Any Switch (rgthree), Any Switch (rgthree), SetNode, GetNode, GetNode, GetNode, Any Switch (rgthree), SetNode, Any Switch (rgthree), SetNode, GetNode]
patterns: []
missing: []
---

# 平台全量/Cc菜Minimax h3 多帧+参考+长视频+独立lora(Runninghub双段版)_2117554822529503234.json

> 来源文件 `comfyui_library/workflows/平台全量/Cc菜Minimax h3 多帧+参考+长视频+独立lora(Runninghub双段版)_2117554822529503234.json`

## 结构

**生成流程**：Model → Latent → Sampling → Process → Output → Other

**节点**（175 个）：
- `SetNode`
- `VAELoader`
- `CLIPLoader`
- `KSamplerSelect` ★核心
- `SetNode`
- `ResolutionSelector`
- `Fast Bypasser (rgthree)`
- `LoadImage`
- `LoadImage`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CreateVideo`
- `GetNode`
- `GetNode`
- `ComfyMathExpression`
- `SetNode`
- `ComfyMathExpression`
- `GetNode`
- `ComfyMathExpression`
- `SetNode`
- `Any Switch (rgthree)`
- `Any Switch (rgthree)`
- `Any Switch (rgthree)`
- `VRGDG_MiniMaxH3AudioDrive`
- `MiniMaxH3AddGuide`
- `GetNode`
- `CreateVideo`
- `SetNode`
- `SetNode`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `VRGDG_MiniMaxH3AudioDrive`
- `PrimitiveFloat`
- `PrimitiveFloat`
- `MiniMaxH3AddGuide`
- `LoadImage`
- `SaveVideo`
- `SetNode`
- `VAELoader`
- `SetNode`
- `LoadAudio`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `Fast Bypasser (rgthree)`
- `TrimAudioDuration`
- `MiniMaxH3AddGuide`
- `MiniMaxH3ReferenceToVideo`
- `Reroute`
- `MiniMaxH3AddGuide`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxH3AddGuide`
- `BasicScheduler`
- `VHS_LoadVideoPath`
- `MarkdownNote`
- `MiniMaxH3AddGuide`
- `LoadImage`
- `MiniMaxH3AddGuide`
- `LoadImage`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `KSamplerSelect` ★核心
- `SetNode`
- `SetNode`
- `BasicScheduler`
- `ManualSigmas`
- `Reroute`
- `GetNode`
- `ModelPreviewOverrideKJ`
- `GetNode`
- `GetNode`
- `SetNode`
- `ModelPreviewOverrideKJ`
- `GetNode`
- `GetNode`
- `Reroute`
- `Any Switch (rgthree)`
- `GetNode`
- `GetNode`
- `GetNode`
- `MiniMaxH3SemanticBridgeConfigT8`
- `MiniMaxH3SemanticBridgeApplyT8`
- `MiniMaxH3SemanticBridgeConfigT8`
- `MiniMaxH3SemanticBridgeApplyT8`
- `ImageFromBatch`
- `TrimAudioDuration`
- `ManualSigmas`
- `ManualSigmas`
- `ManualSigmas`
- `MarkdownNote`
- `MarkdownNote`
- `WanEx_VideoColorMatch`
- `ManualSigmas`
- `ManualSigmas`
- `LoraLoaderModelOnly` ★核心
- `忽略多组孤海`
- `忽略多组孤海`
- `忽略多组孤海`
- `忽略多组孤海`
- `忽略多组孤海`
- `忽略多组孤海`
- `忽略多组孤海`
- `3000688f-5a2b-435a-9a09-b8b8cf4dfda5`
- `TrimAudioDuration`
- `LoadAudio`
- `TrimAudioDuration`
- `LoadAudio`
- `TrimAudioDuration`
- `LoadAudio`
- `忽略多组孤海`
- `忽略多组孤海`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `GoohaiUniversalSlider`
- `忽略多组孤海`
- `忽略多组孤海`
- `LoraLoaderModelOnly` ★核心
- `GoohaiUniversalSlider`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `VHS_LoadVideo`
- `VHS_LoadVideo`
- `VHS_LoadVideo`
- `VHS_LoadVideo`
- `LoraLoaderModelOnly` ★核心
- `Fast Groups Muter (rgthree)`
- `GetNode`
- `GetNode`
- `3860701b-afbc-4fc6-8627-77d475b3f0cb`
- `Text`
- `216f7681-5aed-48b7-a1ca-9cdceaa9cea0`
- `Text`
- `b3e2b2b0-1f68-4478-ac79-5d00ccb733ae`
- `SetNode`
- `c92f4563-479c-4ac9-aa17-7b8843e30c35`
- `AD_video_merge`
- `SetNode`
- `Any Switch (rgthree)`
- `Any Switch (rgthree)`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Any Switch (rgthree)`
- `SetNode`
- `Any Switch (rgthree)`
- `SetNode`
- `GetNode`

## 知识

覆盖率 **61%**（106/175）

**有卡**：`VAELoader`、`CLIPLoader`、`KSamplerSelect`、`ResolutionSelector`、`Fast Bypasser (rgthree)`、`LoadImage`、`CreateVideo`、`ComfyMathExpression`、`VRGDG_MiniMaxH3AudioDrive`、`MiniMaxH3AddGuide`、`SaveVideo`、`LoadAudio`、`TrimAudioDuration`、`MiniMaxH3ReferenceToVideo`、`BasicScheduler`、`VHS_LoadVideoPath`、`VHS_VideoCombine`、`LoraLoaderModelOnly`、`ManualSigmas`、`ModelPreviewOverrideKJ`、`MiniMaxH3SemanticBridgeConfigT8`、`MiniMaxH3SemanticBridgeApplyT8`、`ImageFromBatch`、`WanEx_VideoColorMatch`、`忽略多组孤海`、`3000688f-5a2b-435a-9a09-b8b8cf4dfda5`、`GoohaiUniversalSlider`、`UNETLoader`、`VHS_LoadVideo`、`3860701b-afbc-4fc6-8627-77d475b3f0cb`、`Text`、`216f7681-5aed-48b7-a1ca-9cdceaa9cea0`、`b3e2b2b0-1f68-4478-ac79-5d00ccb733ae`、`c92f4563-479c-4ac9-aa17-7b8843e30c35`、`AD_video_merge`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect、ModelPreviewOverrideKJ
