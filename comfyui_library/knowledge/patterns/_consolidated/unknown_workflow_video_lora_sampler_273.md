---
name: unknown_workflow_video_lora_sampler_273
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.86175
common_nodes: [LayerUtility: PurgeVRAM, LoadImage, LoadWanVideoClipTextEncoder, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoImageClipEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/万能通用测试万相lora_1942490603743555586.json, 视频生成/图生视频/双人2对打wan2.1万相图生视频120_1941226969910689794.json, 视频生成/图生视频/改进版360旋转万相图生视48_1941218870319595522.json, 视频生成/图生视频/环绕自下而上360镜头wan2.1万相图生视60_1941220218918301698.json, 视频生成/图生视频/环绕自下而上360镜头wan2.1万相图生视60_1941765347643125762.json, 视频生成/图生视频/补036_1944753394462674945.json, 视频生成/图生视频/通用测试lors万相_1942526282015911937.json, 视频生成/图生视频/高清版：拉近眼睛镜头万相图生视48工作流_1941194683714584578.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_273

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/万能通用测试万相lora_1942490603743555586.json、视频生成/图生视频/双人2对打wan2.1万相图生视频120_1941226969910689794.json、视频生成/图生视频/改进版360旋转万相图生视48_1941218870319595522.json、视频生成/图生视频/环绕自下而上360镜头wan2.1万相图生视60_1941220218918301698.json、视频生成/图生视频/环绕自下而上360镜头wan2.1万相图生视60_1941765347643125762.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 8 个 workflow 都包含：
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoadWanVideoClipTextEncoder`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoImageClipEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 7/8 个有
- `WanVideoTorchCompileSettings` —— 6/8 个有
- `easy cleanGpuUsed` —— 5/8 个有
- `Int` —— 3/8 个有
- `easy showAnything` —— 3/8 个有
- `Any Switch (rgthree)` —— 2/8 个有
- `easy float` —— 2/8 个有
- `GetNode` —— 1/8 个有
- `MathExpression|pysssss` —— 1/8 个有
- `SetNode` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
