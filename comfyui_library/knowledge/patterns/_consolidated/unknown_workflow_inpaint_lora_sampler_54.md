---
name: unknown_workflow_inpaint_lora_sampler_54
type: Unknown Workflow
frequency: 2
level: weak
coverage: 1
common_nodes: [CLIPTextEncode, CLIPTextEncodeFlux, DeepTranslatorTextNode, DualCLIPLoader, InpaintModelConditioning, KSamplerAdvanced, LoadImage, NunchakuFluxDiTLoader, NunchakuFluxLoraLoader, SaveImage, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/nunchaku双截棍加速 flux-fill-removalv2 人或物体消除_1970470131946168322.json, 图片生成/图生图/removal-flux-fill-v2 物体消除_1931240992354009090.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_lora_sampler_54

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/nunchaku双截棍加速 flux-fill-removalv2 人或物体消除_1970470131946168322.json、图片生成/图生图/removal-flux-fill-v2 物体消除_1931240992354009090.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：100%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPTextEncodeFlux`
- `DeepTranslatorTextNode`
- `DualCLIPLoader`
- `InpaintModelConditioning`
- `KSamplerAdvanced`
- `LoadImage`
- `NunchakuFluxDiTLoader`
- `NunchakuFluxLoraLoader`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageConcatMulti` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 2 | 100% |
| Prompt 约束强度(CFG) | 25 | - | 2 | 100% |
| 采样算法 | 8 | - | 2 | 100% |
| 调度器 | euler_ancestral | - | 2 | 100% |
| 重绘幅度 | normal | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，2 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 25，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 中位数 8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler_ancestral，2 个样本，一致性 100%
- 重绘幅度 最常用 normal，2 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 25，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
