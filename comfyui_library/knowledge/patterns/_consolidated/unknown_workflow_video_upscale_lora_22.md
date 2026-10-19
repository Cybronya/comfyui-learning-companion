---
name: unknown_workflow_video_upscale_lora_22
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.627
common_nodes: [Anything Everywhere, LoadWanVideoT5TextEncoder, RIFE VFI, SetNode, Text Prompt (JPS), UpscaleModelLoader, VHS_VideoCombine, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader, easy cleanGpuUsed, easy clearCacheAll]
problems: []
missing: []
members: [视频生成/图生视频/1937762815677763586.json, 视频生成/图生视频/1937763177356509185.json, 视频生成/文生视频/[免费课程对应工作流] Wrapper-SelfForcing-TextToVideo-60FPS_1937520782014595074.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_lora_22

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/1937762815677763586.json、视频生成/图生视频/1937763177356509185.json、视频生成/文生视频/[免费课程对应工作流] Wrapper-SelfForcing-TextToVideo-60FPS_1937520782014595074.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：63%

## 共有节点

全部 3 个 workflow 都包含：
- `Anything Everywhere`
- `LoadWanVideoT5TextEncoder`
- `RIFE VFI`
- `SetNode`
- `Text Prompt (JPS)`
- `UpscaleModelLoader`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`
- `easy clearCacheAll`

**可变部分**（部分 workflow 才有）：
- `Int` —— 2/3 个有
- `WanVideoBlockSwap` —— 2/3 个有
- `WanVideoEmptyEmbeds` —— 2/3 个有
- `CLIPVisionLoader` —— 1/3 个有
- `GetNode` —— 1/3 个有
- `ImageScale` —— 1/3 个有
- `LoadImage` —— 1/3 个有
- `WanVideoImageClipEncode` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
