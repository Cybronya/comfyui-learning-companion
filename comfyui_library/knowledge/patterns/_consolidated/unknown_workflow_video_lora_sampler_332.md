---
name: unknown_workflow_video_lora_sampler_332
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.911667
common_nodes: [ImageResizeKJv2, LoadImage, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTeaCache, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [图片生成/图生图/【遇见AI】wan2.1 FLF2V首尾帧_2062460186090106881.json, 图片生成/图生图/【遇见AI】wan2.1 MAGREF 单图参考视频_2073698648294252546.json, 图片生成/图生图/【遇见AI】wan2.1 VACE 动作迁移 姿势参考 视频+参考图+提示词_2065246090865238018.json, 图片生成/图生图/【遇见AI】wan2.1 VACE 双图参考_2065243958179094530.json, 图片生成/图生图/【遇见AI】wan2.1 VACE 视频重绘，换脸，修改任何东西_2065246575059886081.json, 视频生成/图生视频/【遇见AI】wan2.1 VACE 动作迁移 姿势参考 视频+提示词_2065244368470106114.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_332

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/【遇见AI】wan2.1 FLF2V首尾帧_2062460186090106881.json、图片生成/图生图/【遇见AI】wan2.1 MAGREF 单图参考视频_2073698648294252546.json、图片生成/图生图/【遇见AI】wan2.1 VACE 动作迁移 姿势参考 视频+参考图+提示词_2065246090865238018.json、图片生成/图生图/【遇见AI】wan2.1 VACE 双图参考_2065243958179094530.json、图片生成/图生图/【遇见AI】wan2.1 VACE 视频重绘，换脸，修改任何东西_2065246575059886081.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 6 个 workflow 都包含：
- `ImageResizeKJv2`
- `LoadImage`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTeaCache`
- `WanVideoTextEncodeCached`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 4/6 个有
- `WanVideoVACEEncode` —— 4/6 个有
- `WanVideoVACEModelSelect` —— 4/6 个有
- `VHS_LoadVideo` —— 3/6 个有
- `AIO_Preprocessor` —— 2/6 个有
- `CLIPVisionLoader` —— 2/6 个有
- `MaskPreview+` —— 2/6 个有
- `VHS_VideoInfo` —— 2/6 个有
- `WanVideoClipVisionEncode` —— 2/6 个有
- `WanVideoImageToVideoEncode` —— 2/6 个有
- `Image Overlay` —— 1/6 个有
- `ImageScale` —— 1/6 个有
- `InpaintPreprocessor` —— 1/6 个有
- `InvertMask` —— 1/6 个有
- `LayerMask: LoadSegmentAnythingModels` —— 1/6 个有
- `LayerMask: RmBgUltra V2` —— 1/6 个有
- `LayerMask: SegmentAnythingUltra V3` —— 1/6 个有
- `easy makeImageForICLora` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
