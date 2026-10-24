---
name: unknown_workflow_controlnet_sampler_clip_27
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8795
common_nodes: [AIO_Preprocessor, CLIPLoader, CLIPTextEncode, ControlNetApplyAdvanced, ControlNetLoader, EmptySD3LatentImage, KSampler, LoadImage, ModelSamplingAuraFlow, NunchakuQwenImageDiTLoader, PreviewImage, SaveImage, SetUnionControlNetType, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Nunchaku-Qwen-image +Controlnet-union加速工作流_2073060605287821314.json, 图片生成/文生图/Nunchaku-Qwen-image +Controlnet-union加速工作流_1966880594737106946.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_sampler_clip_27

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Nunchaku-Qwen-image +Controlnet-union加速工作流_2073060605287821314.json、图片生成/文生图/Nunchaku-Qwen-image +Controlnet-union加速工作流_1966880594737106946.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：88%

## 共有节点

全部 2 个 workflow 都包含：
- `AIO_Preprocessor`
- `CLIPLoader`
- `CLIPTextEncode`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `EmptySD3LatentImage`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `NunchakuQwenImageDiTLoader`
- `PreviewImage`
- `SaveImage`
- `SetUnionControlNetType`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AILab_MiniCPM_4_V` —— 1/2 个有
- `GLM_Vision_ImageToPrompt` —— 1/2 个有
- `JjkText` —— 1/2 个有
- `ShowText` —— 1/2 个有
- `Switch` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 1 | - | 2 | 100% |
| 采样步数 | 8 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- ControlNet 权重 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
