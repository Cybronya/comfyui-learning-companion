---
name: unknown_workflow_video_lora_sampler_571
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.89625
common_nodes: [CreateCFGScheduleFloatList, GetImageSizeAndCount, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Wan 2.2 图生视频（优化版）_1951564039392579586.json, 视频生成/文生视频/Wan 2.2 文生视频（优化版）_1951554035532902402.json, 视频生成/文生视频/通义万相wan2.2文生视频（kj加速版6步+提示词自动优化）_1950555101742223362.json, 视频生成/文生视频/通义万相wan2.2文生视频（kj加速版6步）_1950435690355015681.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_571

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/Wan 2.2 图生视频（优化版）_1951564039392579586.json、视频生成/文生视频/Wan 2.2 文生视频（优化版）_1951554035532902402.json、视频生成/文生视频/通义万相wan2.2文生视频（kj加速版6步+提示词自动优化）_1950555101742223362.json、视频生成/文生视频/通义万相wan2.2文生视频（kj加速版6步）_1950435690355015681.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 4 个 workflow 都包含：
- `CreateCFGScheduleFloatList`
- `GetImageSizeAndCount`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `MathExpression|pysssss` —— 3/4 个有
- `RH_LLMAPI_NODE` —— 3/4 个有
- `WanVideoEmptyEmbeds` —— 3/4 个有
- `ImpactSwitch` —— 2/4 个有
- `Primitive integer [Crystools]` —— 2/4 个有
- `SeargePromptText` —— 2/4 个有
- `ShowText` —— 2/4 个有
- `Text Multiline` —— 2/4 个有
- `easy cleanGpuUsed` —— 2/4 个有
- `ImageResize+` —— 1/4 个有
- `LoadImage` —— 1/4 个有
- `ShowText|pysssss` —— 1/4 个有
- `Wan22PromptSelector` —— 1/4 个有
- `WanVideoImageToVideoEncode` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
