---
name: unknown_workflow_video_sampler_vae_42
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.8614
common_nodes: [ImageResizeKJ, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoModelLoader, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1935000181781766145.json, 视频生成/图生视频/1894640699545944065.json, 视频生成/图生视频/1930311338440998914.json, 视频生成/图生视频/1930415960338108418.json, 视频生成/图生视频/1896450417918345217.json, 视频生成/图生视频/1917932584058425345.json, 视频生成/图生视频/1917823045400985602.json, 视频生成/图生视频/1917833994954539009.json, 视频生成/图生视频/1914283396808306690.json, 视频生成/图生视频/1913412975162552322.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_42

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/1935000181781766145.json、视频生成/图生视频/1894640699545944065.json、视频生成/图生视频/1930311338440998914.json、视频生成/图生视频/1930415960338108418.json、视频生成/图生视频/1896450417918345217.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 10 个 workflow 都包含：
- `ImageResizeKJ`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPVisionLoader` —— 8/10 个有
- `WanVideoClipVisionEncode` —— 8/10 个有
- `WanVideoImageToVideoEncode` —— 8/10 个有
- `WanVideoLoraSelect` —— 8/10 个有
- `WanVideoBlockSwap` —— 7/10 个有
- `PreviewImage` —— 6/10 个有
- `WanVideoTorchCompileSettings` —— 6/10 个有
- `LoadWanVideoClipTextEncoder` —— 2/10 个有
- `SaveAnimatedWEBP` —— 2/10 个有
- `WanVideoImageClipEncode` —— 2/10 个有
- `WanVideoVRAMManagement` —— 2/10 个有
- `ColorMatch` —— 1/10 个有
- `INTConstant` —— 1/10 个有
- `ImageScaleToTotalPixels` —— 1/10 个有
- `easy imageSize` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
