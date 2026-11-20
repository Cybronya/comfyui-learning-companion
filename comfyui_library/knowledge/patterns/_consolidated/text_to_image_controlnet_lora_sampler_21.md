---
name: text_to_image_controlnet_lora_sampler_21
type: Text To Image
frequency: 2
level: weak
coverage: 0.936
common_nodes: [AIO_Preprocessor, CLIPTextEncode, ConditioningZeroOut, ControlNetApplySD3, ControlNetLoader, DualCLIPLoader, EmptyLatentImage, KSampler, LoadImage, LoraLoader, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/FLUX+模特姿势动作控制（大牌运动模特）V1.13_1914983446777688066.json, 图片生成/文生图/FLUX-ControlNet Union Pro_1988619898043719681.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_lora_sampler_21

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/FLUX+模特姿势动作控制（大牌运动模特）V1.13_1914983446777688066.json、图片生成/文生图/FLUX-ControlNet Union Pro_1988619898043719681.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：94%

## 共有节点

全部 2 个 workflow 都包含：
- `AIO_Preprocessor`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `ControlNetApplySD3`
- `ControlNetLoader`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `LoraLoader`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DWPreprocessor` —— 1/2 个有
- `DepthAnythingV2Preprocessor` —— 1/2 个有
- `ETN_Translate` —— 1/2 个有
- `FluxGuidance` —— 1/2 个有
- `ImageResize+` —— 1/2 个有
- `LP-TranslateToEN` —— 1/2 个有
- `LayerUtility: JoyCaptionBeta1` —— 1/2 个有
- `LayerUtility: LoadJoyCaptionBeta1Model` —— 1/2 个有
- `SetUnionControlNetType` —— 1/2 个有
- `easy imageSize` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.66 | - | 2 | 79% |
| LoRA 模型强度 | 0.7 | - | 2 | 57% |
| LoRA 文本强度 | 0.65 | - | 2 | 46% |
| 采样步数 | 22.5 | - | 2 | 89% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | deis | - | 2 | 50% |
| 调度器 | beta | - | 2 | 50% |
| 重绘幅度 | 1 | - | 2 | 100% |
| 宽度 | 1280 | - | 2 | 80% |
| 高度 | 768 | - | 2 | 67% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.66，样本不足，未给区间，2 个样本
- LoRA 模型强度 中位数 0.7，样本不足，未给区间，2 个样本
- LoRA 文本强度 中位数 0.65，样本不足，未给区间，2 个样本，取值分散，一致性仅 46%
- 采样步数 中位数 22.5，样本不足，未给区间，2 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 deis，2 个样本，一致性 50%
- 调度器 最常用 beta，2 个样本，一致性 50%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 1280，样本不足，未给区间，2 个样本，取值集中（一致性 80%）
- 高度 中位数 768，样本不足，未给区间，2 个样本
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
