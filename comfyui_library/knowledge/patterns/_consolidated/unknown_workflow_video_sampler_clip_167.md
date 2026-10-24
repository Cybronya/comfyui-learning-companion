---
name: unknown_workflow_video_sampler_clip_167
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.933
common_nodes: [LoadImage, LoadWanVideoClipTextEncoder, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageClipEncode, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/文生视频/CG迷-360度旋转 Wan视频Lora视频生成_1927330621041827842.json, 视频生成/文生视频/WAN2.1万相图生视频_1900012001182244866.json, 视频生成/文生视频/Wan2.1图生视频-拥抱_1948418941659021313.json, 视频生成/文生视频/wan2.1美女跳舞 细节完美 不崩脸_1922456339556028417.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_167

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/文生视频/CG迷-360度旋转 Wan视频Lora视频生成_1927330621041827842.json、视频生成/文生视频/WAN2.1万相图生视频_1900012001182244866.json、视频生成/文生视频/Wan2.1图生视频-拥抱_1948418941659021313.json、视频生成/文生视频/wan2.1美女跳舞 细节完美 不崩脸_1922456339556028417.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 4 个 workflow 都包含：
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
- `WanVideoLoraSelect` —— 3/4 个有
- `CR Text` —— 1/4 个有
- `CR Text Replace` —— 1/4 个有
- `ShowText|pysssss` —— 1/4 个有
- `WanVideoExperimentalArgs` —— 1/4 个有
- `WanVideoSLG` —— 1/4 个有
- `WanVideoTeaCache` —— 1/4 个有
- `WanVideoTorchCompileSettings` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
