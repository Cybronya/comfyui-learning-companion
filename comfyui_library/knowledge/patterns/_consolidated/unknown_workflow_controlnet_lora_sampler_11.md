---
name: unknown_workflow_controlnet_lora_sampler_11
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.9028
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, ControlNetLoader, DualCLIPLoader, FluxGuidance, InfiniteYouApply, KSamplerSelect, LoadImage, LoraLoaderModelOnly, PreviewImage, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/一键人脸融合写真_1906653077070614530.json, 图片生成/图生图/完美InfiniteYou换脸图生图(脸部朝向可变)_1906570674301751297.json, 图片生成/文生图/InfiniteYou换脸写真(脸朝向不在固定)_1905916756995805185.json, 图片生成/文生图/最新InfiniteYou完美换脸文生图(脸部朝向可变)_1906558127117111297.json, 图片生成/文生图/预测未来子女-InfiniteYou脸部融合_1905921936663171074.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_lora_sampler_11

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/一键人脸融合写真_1906653077070614530.json、图片生成/图生图/完美InfiniteYou换脸图生图(脸部朝向可变)_1906570674301751297.json、图片生成/文生图/InfiniteYou换脸写真(脸朝向不在固定)_1905916756995805185.json、图片生成/文生图/最新InfiniteYou完美换脸文生图(脸部朝向可变)_1906558127117111297.json、图片生成/文生图/预测未来子女-InfiniteYou脸部融合_1905921936663171074.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `ControlNetLoader`
- `DualCLIPLoader`
- `FluxGuidance`
- `InfiniteYouApply`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR SDXL Aspect Ratio` —— 4/5 个有
- `LayerMask: PersonMaskUltra V2` —— 4/5 个有
- `LayerUtility: CropByMask V2` —— 4/5 个有
- `RH_Captioner` —— 4/5 个有
- `ShowText|pysssss` —— 4/5 个有
- `Text Concatenate (JPS)` —— 4/5 个有
- `Text Multiline` —— 4/5 个有
- `EmptySD3LatentImage` —— 3/5 个有
- `FaceCombine` —— 3/5 个有
- `Fast Groups Bypasser (rgthree)` —— 3/5 个有
- `KSampler` —— 3/5 个有
- `ImageConcatMulti` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 30 - 30 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，观测区间 30 - 30，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
