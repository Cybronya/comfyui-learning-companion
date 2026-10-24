---
name: unknown_workflow_lora_sampler_clip_57
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.835143
common_nodes: [CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, ConditioningZeroOut, DualCLIPLoader, FramePackFindNearestBucket, FramePackLoraSelect, FramePackSingleFrameSampler, ImageResize+, JWInteger, LoadFramePackModel, LoadImage, SaveImage, VAEDecodeTiled, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/FramePack 人物动作编辑_1933859523817820161.json, 图片生成/图生图/FramePack 图生图｜动漫换背景_1935152830489796610.json, 图片生成/图生图/FramePack单图动作编辑_1945759748434305026.json, 图片生成/图生图/FramePack图像编辑-单帧动作编辑V1_1932773456045821954.json, 图片生成/图生图/FramePack图像编辑（人物一致性多图动作参考）V1_1932773473997787138.json, 图片生成/图生图/非常好用！FramePack图像编辑-单帧动作编辑_1933156434433744898.json, 视频生成/图生视频/动漫换背景打光-FramePack单帧图编辑_1935136983549157377.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_57

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/FramePack 人物动作编辑_1933859523817820161.json、图片生成/图生图/FramePack 图生图｜动漫换背景_1935152830489796610.json、图片生成/图生图/FramePack单图动作编辑_1945759748434305026.json、图片生成/图生图/FramePack图像编辑-单帧动作编辑V1_1932773456045821954.json、图片生成/图生图/FramePack图像编辑（人物一致性多图动作参考）V1_1932773473997787138.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FramePackFindNearestBucket`
- `FramePackLoraSelect`
- `FramePackSingleFrameSampler`
- `ImageResize+`
- `JWInteger`
- `LoadFramePackModel`
- `LoadImage`
- `SaveImage`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 6/7 个有
- `ImageConcatMulti` —— 6/7 个有
- `FramePackTorchCompileSettings` —— 5/7 个有
- `GetNode` —— 4/7 个有
- `SetNode` —— 4/7 个有
- `Image Rembg (Remove Background)` —— 2/7 个有
- `PreviewImage` —— 2/7 个有
- `ChinesePrompt_Mix` —— 1/7 个有
- `Fast Groups Bypasser (rgthree)` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
