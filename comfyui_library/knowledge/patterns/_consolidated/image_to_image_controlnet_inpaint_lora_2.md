---
name: image_to_image_controlnet_inpaint_lora_2
type: Image To Image
frequency: 11
level: strong
coverage: 0.879273
common_nodes: [CLIPLoader, CLIPTextEncode, ControlNetInpaintingAliMamaApply, ControlNetLoader, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-局部重绘-简单好用_1992207282454810626.json, 图片生成/图生图/Qwen-局部重绘超简单_1991433574167629825.json, 图片生成/图生图/Qwen千问扩图【加速 LoRA 提速版】：原版 fp8_e4m3f + 低配 GGUF_1986436217229242370.json, 图片生成/图生图/Qwen局部重绘【加速 LoRA 提速版】：原版 fp8_e4m3f + 低配 GGUF_1986430416326426625.json, 图片生成/图生图/Qwen局部重绘【加速 LoRA 提速版】：原版 fp8_e4m3f + 低配 GGUF_2006612109051830274.json, 图片生成/图生图/Qwen局部重绘【加速_LoRA_提速版】_原版_fp8_e4m3f_+_低配_GGUF_2063623655715860481.json, 图片生成/图生图/qwen image fp8-局部重绘_1986852657413468162.json, 图片生成/图生图/一键扩图！Qwen image InstanX_1990241554310852609.json, 图片生成/图生图/千问局部重绘 (1)_2009523394458423297.json, 图片生成/图生图/千问局部重绘 (1)_2047649278096576514.json, 图片生成/图生图/千问扩图工作流 (1)_2009525416305893378.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_inpaint_lora_2

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/Qwen-局部重绘-简单好用_1992207282454810626.json、图片生成/图生图/Qwen-局部重绘超简单_1991433574167629825.json、图片生成/图生图/Qwen千问扩图【加速 LoRA 提速版】：原版 fp8_e4m3f + 低配 GGUF_1986436217229242370.json、图片生成/图生图/Qwen局部重绘【加速 LoRA 提速版】：原版 fp8_e4m3f + 低配 GGUF_1986430416326426625.json、图片生成/图生图/Qwen局部重绘【加速 LoRA 提速版】：原版 fp8_e4m3f + 低配 GGUF_2006612109051830274.json…）

- **类型**：Image To Image
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ControlNetInpaintingAliMamaApply`
- `ControlNetLoader`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 10/11 个有
- `PDImageResizeV2` —— 9/11 个有
- `ConditioningZeroOut` —— 8/11 个有
- `ImageAndMaskPreview` —— 7/11 个有
- `UnetLoaderGGUF` —— 7/11 个有
- `ModelSamplingAuraFlow` —— 4/11 个有
- `CLIPLoaderGGUF` —— 3/11 个有
- `ImagePadForOutpaint` —— 3/11 个有
- `LayerUtility: PurgeVRAM` —— 2/11 个有
- `MuyeTextEditOutput` —— 2/11 个有
- `Anything Everywhere3` —— 1/11 个有
- `CR Text` —— 1/11 个有
- `ImageResizeKJv2` —— 1/11 个有
- `PrimitiveInt` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 8 | 11 | 82% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 11 | 100% |
| 采样算法 | euler | - | 11 | 100% |
| 调度器 | simple | - | 11 | 91% |
| 重绘幅度 | 1 | 0.8 - 1 | 11 | 92% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 8，11 个样本，取值集中（一致性 82%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，11 个样本，一致性 100%
- 调度器 最常用 simple，11 个样本，一致性 91%
- 重绘幅度 中位数 1，观测区间 0.8 - 1，11 个样本，取值集中（一致性 92%）
- 高发问题（11/11 个样本）：Steps较低可能导致细节不足
