---
name: image_to_image_lora_sampler_unet_29
type: Image To Image
frequency: 17
level: strong
coverage: 0.881882
common_nodes: [CFGNorm, CLIPLoader, FluxKontextImageScale, FluxKontextMultiReferenceLatentMethod, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: []
members: [图片生成/图生图/Qwen-Camera_2068695632642142209.json, 图片生成/图生图/Qwen-Edit-2511 单图、多图编辑工作流_2091504533078888449.json, 图片生成/图生图/Qwen-Edit-2511 场景多角度工作流_2091522931443716097.json, 图片生成/图生图/Qwen-Edit-2511 场景自定义角度工作流_2091520586739699713.json, 图片生成/图生图/Qwen-Edit-2511 溶图打光工作流_2091511848628740097.json, 图片生成/图生图/Qwen-Edit-2511_单图、多图编辑工作流_2096512805334769666.json, 图片生成/图生图/Qwen-Edit-2511_单图、多图编辑工作流_2096870533769027586.json, 图片生成/图生图/QwenEdit2511多图编辑工作流_2058767665044480001.json, 图片生成/图生图/场景多角度分镜3.0制作镜头qwen2511风格一致性分镜加速版3.0qwenedit2511加速版_2009533490206871553.json, 图片生成/图生图/场景多角度分镜3.0制作镜头qwen2511风格一致性分镜加速版3.0qwenedit2511加速版_2083366341913960449.json, 图片生成/图生图/场景多角度分镜3.0制作镜头qwen2511风格一致性分镜加速版3.0qwenedit2511加速版_2083375355112550402.json, 图片生成/图生图/场景多角度分镜3.0制作镜头qwen2511风格一致性分镜加速版3.0qwenedit2511加速版_2091742231643381762.json, 图片生成/图生图/场景多角度分镜3.0制作镜头qwen2511风格一致性分镜加速版3.0qwenedit2511加速版_2101961996269871105.json, 图片生成/图生图/场景多角度分镜4.0((九视角）制作镜头qwen2511风格一致性分镜加速版4.0_2018924258122010625.json, 图片生成/图生图/多场景 多角度 分镜制作 qwen2511 风格一致性 分镜加速版3.0_2046210559363780610.json, 图片生成/图生图/多视角影视人物多视角加速版（常用视角）_2009573649203863554.json, 平台全量/自由摄像机 场景多角度分镜 不同分镜头qwen2511风格一致 分镜_2047129079220019202.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_29

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（图片生成/图生图/Qwen-Camera_2068695632642142209.json、图片生成/图生图/Qwen-Edit-2511 单图、多图编辑工作流_2091504533078888449.json、图片生成/图生图/Qwen-Edit-2511 场景多角度工作流_2091522931443716097.json、图片生成/图生图/Qwen-Edit-2511 场景自定义角度工作流_2091520586739699713.json、图片生成/图生图/Qwen-Edit-2511 溶图打光工作流_2091511848628740097.json…）

- **类型**：Image To Image
- **样本数**：17
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 17 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `FluxKontextImageScale`
- `FluxKontextMultiReferenceLatentMethod`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `VAEDecode` —— 16/17 个有
- `CR Prompt List` —— 10/17 个有
- `PreviewAny` —— 10/17 个有
- `Text Multiline` —— 10/17 个有
- `PreviewImage` —— 7/17 个有
- `Image Comparer (rgthree)` —— 5/17 个有
- `EmptySD3LatentImage` —— 3/17 个有
- `QwenMultiangleCameraNode` —— 2/17 个有
- `DapaoImageAspectRatioResizeNode` —— 1/17 个有
- `Int` —— 1/17 个有
- `StringConcat|Mie` —— 1/17 个有
- `VAEDecodeTiled` —— 1/17 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 17 | 66% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 17 | 100% |
| 采样算法 | euler | - | 17 | 100% |
| 调度器 | simple | - | 17 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 17 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 17/17 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |
| 发现KSampler但没有VAEDecode | 1/17 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，17 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，17 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，17 个样本，一致性 100%
- 调度器 最常用 simple，17 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，17 个样本，取值集中（一致性 100%）
- 高发问题（17/17 个样本）：Steps较低可能导致细节不足
