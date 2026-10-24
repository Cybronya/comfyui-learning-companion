---
name: image_to_image_controlnet_inpaint_lora_20
type: Image To Image
frequency: 2
level: weak
coverage: 0.771
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, ControlNetInpaintingAliMamaApply, ControlNetLoader, IO_input_any, Image Comparer (rgthree), ImagePadForOutpaint, ImageResize+, Image_Resize_sum, KSampler, LoadImage, LoraLoaderModelOnly, MaskPreview+, ModelSamplingAuraFlow, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, easy clearCacheAll, easy imageSize, math_calculate]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/尺寸修改_2052299227107213314.json, 图片生成/图生图/通过扩图实现图片任意尺寸修改_2050873089453506562.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_inpaint_lora_20

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/尺寸修改_2052299227107213314.json、图片生成/图生图/通过扩图实现图片任意尺寸修改_2050873089453506562.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：77%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `ControlNetInpaintingAliMamaApply`
- `ControlNetLoader`
- `IO_input_any`
- `Image Comparer (rgthree)`
- `ImagePadForOutpaint`
- `ImageResize+`
- `Image_Resize_sum`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaskPreview+`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `easy imageSize`
- `math_calculate`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1.2 | - | 2 | 100% |
| 采样算法 | dpmpp_2m_sde_gpu | - | 2 | 100% |
| 调度器 | karras | - | 2 | 100% |
| 重绘幅度 | 0.95 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1.2，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_2m_sde_gpu，2 个样本，一致性 100%
- 调度器 最常用 karras，2 个样本，一致性 100%
- 重绘幅度 中位数 0.95，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
