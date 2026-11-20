---
name: unknown_workflow_controlnet_face_detailer_lora_4
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8265
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, ControlNetApplyAdvanced, ControlNetLoader, FaceDetailer, LoadImage, LoraLoader, PreviewImage, SAMLoader, SaveImage, UltralyticsDetectorProvider]
problems: []
missing: []
members: [平台全量/在线Lora换脸_1890352649911312386.json, 平台全量/姓氏风景_1791013112611196929.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_face_detailer_lora_4

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/在线Lora换脸_1890352649911312386.json、平台全量/姓氏风景_1791013112611196929.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：83%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `FaceDetailer`
- `LoadImage`
- `LoraLoader`
- `PreviewImage`
- `SAMLoader`
- `SaveImage`
- `UltralyticsDetectorProvider`

**可变部分**（部分 workflow 才有）：
- `ConditioningCombine` —— 1/2 个有
- `DWPreprocessor` —— 1/2 个有
- `EmptyLatentImage` —— 1/2 个有
- `KSamplerAdvanced` —— 1/2 个有
- `VAEDecode` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.975 | - | 2 | 51% |
| LoRA 模型强度 | 0.575 | - | 2 | 96% |
| LoRA 文本强度 | 0.9 | - | 2 | 89% |
| 采样步数 | randomize | - | 1 | 100% |
| Prompt 约束强度(CFG) | 30 | - | 1 | 100% |
| 采样算法 | 7 | - | 1 | 100% |
| 调度器 | dpmpp_2m | - | 1 | 100% |
| 重绘幅度 | karras | - | 1 | 100% |
| 宽度 | 1024 | - | 1 | 100% |
| 高度 | 1024 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.975，样本不足，未给区间，2 个样本
- LoRA 模型强度 中位数 0.575，样本不足，未给区间，2 个样本，取值集中（一致性 96%）
- LoRA 文本强度 中位数 0.9，样本不足，未给区间，2 个样本，取值集中（一致性 89%）
- 风险：Prompt 约束强度(CFG) 观测到 30，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
