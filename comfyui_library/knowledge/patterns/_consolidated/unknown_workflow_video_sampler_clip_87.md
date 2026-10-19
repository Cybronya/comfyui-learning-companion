---
name: unknown_workflow_video_sampler_clip_87
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.936
common_nodes: [LoadImage, LoadWanVideoClipTextEncoder, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageClipEncode, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/文生视频/1927330621041827842.json, 视频生成/文生视频/1900012001182244866.json, 视频生成/文生视频/1948418941659021313.json, 视频生成/文生视频/1894956774334595074.json, 视频生成/文生视频/1918935323899006978.json, 视频生成/文生视频/1918185073190047746.json, 视频生成/文生视频/1898157679490060290.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_87

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/文生视频/1927330621041827842.json、视频生成/文生视频/1900012001182244866.json、视频生成/文生视频/1948418941659021313.json、视频生成/文生视频/1894956774334595074.json、视频生成/文生视频/1918935323899006978.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 7 个 workflow 都包含：
- `LoadImage`
- `LoadWanVideoClipTextEncoder`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoImageClipEncode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `WanVideoLoraSelect` —— 4/7 个有
- `CR Upscale Image` —— 3/7 个有
- `RIFE VFI` —— 3/7 个有
- `ImageResizeKJ` —— 2/7 个有
- `WanVideoTorchCompileSettings` —— 2/7 个有
- `easy cleanGpuUsed` —— 2/7 个有
- `CR Text` —— 1/7 个有
- `CR Text Replace` —— 1/7 个有
- `Fast Groups Muter (rgthree)` —— 1/7 个有
- `Note Plus (mtb)` —— 1/7 个有
- `ShowText|pysssss` —— 1/7 个有
- `String Literal` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
