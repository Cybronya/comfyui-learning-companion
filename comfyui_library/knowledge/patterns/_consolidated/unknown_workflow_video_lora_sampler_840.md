---
name: unknown_workflow_video_lora_sampler_840
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.889
common_nodes: [Fast Groups Bypasser (rgthree), ImageBlur, Int, LoadWanVideoT5TextEncoder, RHHiddenNodes, ShowText|pysssss, VHS_LoadVideo, VHS_VideoCombine, WanVideoControlEmbeds, WanVideoDecode, WanVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/wan2.1视频高精度重绘（视频修复）_1908011903803600898.json, 视频生成/文生视频/视频高精度重绘_1932643616856625153.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_840

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/wan2.1视频高精度重绘（视频修复）_1908011903803600898.json、视频生成/文生视频/视频高精度重绘_1932643616856625153.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：89%

## 共有节点

全部 2 个 workflow 都包含：
- `Fast Groups Bypasser (rgthree)`
- `ImageBlur`
- `Int`
- `LoadWanVideoT5TextEncoder`
- `RHHiddenNodes`
- `ShowText|pysssss`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoControlEmbeds`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
