---
name: unknown_workflow_video_lora_sampler_565
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.945
common_nodes: [AudioCrop, AudioSeparation, HuMoEmbeds, ImageBatchMulti, ImageResizeKJv2, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader, WhisperModelLoader, easy imageRemBg]
problems: []
missing: []
members: [图片生成/文生图/ai MV应用版（30S福音）_2000822453771399170.json, 平台全量/MV_1995717867448446978.json, 数字人/数字人/HuMo电商展示产品+口播_1987818616303366146.json, 视频生成/图生视频/👽HuMo电商展示产品+口播👽_1969293960176934913.json, 视频生成/图生视频/👽Humo数字人音乐MV嗨歌版👽_1968957972288323586.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_565

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/ai MV应用版（30S福音）_2000822453771399170.json、平台全量/MV_1995717867448446978.json、数字人/数字人/HuMo电商展示产品+口播_1987818616303366146.json、视频生成/图生视频/👽HuMo电商展示产品+口播👽_1969293960176934913.json、视频生成/图生视频/👽Humo数字人音乐MV嗨歌版👽_1968957972288323586.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 5 个 workflow 都包含：
- `AudioCrop`
- `AudioSeparation`
- `HuMoEmbeds`
- `ImageBatchMulti`
- `ImageResizeKJv2`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`
- `WhisperModelLoader`
- `easy imageRemBg`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 4/5 个有
- `ImpactInt` —— 4/5 个有
- `JWIntegerToString` —— 4/5 个有
- `SimpleMath+` —— 4/5 个有
- `ImageFromBatch` —— 3/5 个有
- `MultiTalkModelLoader` —— 3/5 个有
- `MultiTalkWav2VecEmbeds` —— 3/5 个有
- `PreviewImage` —— 3/5 个有
- `WanVideoCombineEmbeds` —— 3/5 个有
- `WanVideoImageToVideoMultiTalk` —— 3/5 个有
- `WanVideoTorchCompileSettings` —— 3/5 个有
- `Wav2VecModelLoader` —— 3/5 个有
- `CreateCFGScheduleFloatList` —— 2/5 个有
- `ImageConcanate` —— 2/5 个有
- `Seed (rgthree)` —— 2/5 个有
- `AudioCropProcessUTK` —— 1/5 个有
- `CM_FloatUnaryOperation` —— 1/5 个有
- `INTConstant` —— 1/5 个有
- `MathExpression|pysssss` —— 1/5 个有
- `Note Plus (mtb)` —— 1/5 个有
- `PrimitiveString` —— 1/5 个有
- `easy showAnything` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
