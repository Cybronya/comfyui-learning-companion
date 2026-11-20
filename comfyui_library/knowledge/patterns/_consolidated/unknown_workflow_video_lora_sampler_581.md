---
name: unknown_workflow_video_lora_sampler_581
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.983
common_nodes: [CLIPVisionLoader, ImageResizeKJ, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVACEModelSelect, WanVideoVAELoader]
problems: []
missing: []
members: [平台全量/wan2.1模特T台走猫步_1970749317638201346.json, 视频生成/图生视频/wan2.1 法相魔法幻想 视觉特效_2062016628551933953.json, 视频生成/图生视频/wan2.1 法相魔法幻想 视觉特效_2062080584259817473.json, 视频生成/图生视频/wan2.1 法相魔法幻想 视觉特效_2072700454361976834.json, 视频生成/图生视频/wan2.1 法相魔法幻想 视觉特效_2072700639905406978.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_581

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（平台全量/wan2.1模特T台走猫步_1970749317638201346.json、视频生成/图生视频/wan2.1 法相魔法幻想 视觉特效_2062016628551933953.json、视频生成/图生视频/wan2.1 法相魔法幻想 视觉特效_2062080584259817473.json、视频生成/图生视频/wan2.1 法相魔法幻想 视觉特效_2072700454361976834.json、视频生成/图生视频/wan2.1 法相魔法幻想 视觉特效_2072700639905406978.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPVisionLoader`
- `ImageResizeKJ`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVACEModelSelect`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `Primitive integer [Crystools]` —— 4/5 个有
- `Text Multiline` —— 4/5 个有
- `CR SDXL Aspect Ratio` —— 1/5 个有
- `Float` —— 1/5 个有
- `PrimitiveFloat` —— 1/5 个有
- `RH_Translator` —— 1/5 个有
- `SimpleMath+` —— 1/5 个有
- `WanVideoLoraSelectMulti` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
