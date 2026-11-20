---
name: image_to_image_lora_sampler_unet_10
type: Image To Image
frequency: 24
level: strong
coverage: 0.899167
common_nodes: [CFGNorm, CLIPLoader, FluxKontextMultiReferenceLatentMethod, ImageScaleToTotalPixels, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/2511 千问3D摄像头控制_2015017305377349634.json, 图片生成/图生图/2511+可视化灯光调节(重打光lora强化版)_2011008593067253762.json, 图片生成/图生图/2511+可视化灯光调节(重打光lora强化版)_2011649766312124417.json, 图片生成/图生图/2511+可视化灯光调节(重打光lora强化版)_2058374385785982977.json, 图片生成/图生图/2511+多角度+灯光调节合并工作流_2011312094162980866.json, 图片生成/图生图/2511+自动控制镜头（一句话表达人物情绪）_2011032739998339073.json, 图片生成/图生图/2511+镜头多角度选择（柯基大佬版）_2087562742067712001.json, 图片生成/图生图/2511+镜头选择_2010577901594353666.json, 图片生成/图生图/2511+镜头选择_2045054128786776066.json, 图片生成/图生图/2511+镜头选择（柯基大佬版）_2009721085058617345.json, 图片生成/图生图/2511+镜头选择（柯基大佬版）_2009799560096387074.json, 图片生成/图生图/2511+镜头选择（柯基大佬版）_2010534869331353601.json, 图片生成/图生图/2511+镜头选择（柯基大佬版）_2010946894377263105.json, 图片生成/图生图/2511+镜头选择（柯基大佬版）_2010969372407369729.json, 图片生成/图生图/ComfyUI-qwenmultianglelight 基础流_2010897413225062401.json, 图片生成/图生图/QWEN2511+重打光(Relight)_2018262241644126210.json, 图片生成/图生图/Qwen 2511 edit 多视角镜头拍摄 智能多角度生成 qwen image edit_2010692605092306946.json, 图片生成/图生图/Qwen 2511 镜头控制插件_2009786830929010690.json, "图片生成/图生图/Qwen Edit 2511+镜头多角度控制,一张图片变换多个角度_2052204567022063617.json", "图片生成/图生图/Qwen Edit 2511+镜头多角度控制,一张图片变换多个角度_2052916903613607937.json", 图片生成/图生图/Qwen Edit 2511： Multiangle Camera 镜头选择（直观简单好用）_2009796133521989633.json, 图片生成/图生图/Qwen Image Edit 2511+镜头选择 不同视角+镜头选择（柯基大佬版）_2012169391844102146.json, 图片生成/图生图/Qwen Image Edit 2511+镜头选择 不同视角_2011062220834213890.json, 图片生成/图生图/Qwen multiple angle2511+多镜头选择_2009799321264328706.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_10

> 由 `engine/knowledge_consolidation` 从 24 个 workflow 归纳得出（图片生成/图生图/2511 千问3D摄像头控制_2015017305377349634.json、图片生成/图生图/2511+可视化灯光调节(重打光lora强化版)_2011008593067253762.json、图片生成/图生图/2511+可视化灯光调节(重打光lora强化版)_2011649766312124417.json、图片生成/图生图/2511+可视化灯光调节(重打光lora强化版)_2058374385785982977.json、图片生成/图生图/2511+多角度+灯光调节合并工作流_2011312094162980866.json…）

- **类型**：Image To Image
- **样本数**：24
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 24 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `FluxKontextMultiReferenceLatentMethod`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptySD3LatentImage` —— 22/24 个有
- `easy showAnything` —— 22/24 个有
- `QwenMultiangleCameraNode` —— 19/24 个有
- `easy promptList` —— 18/24 个有
- `QwenMultiangleLightningNode` —— 6/24 个有
- `ShowText` —— 2/24 个有
- `EmptyLatentImage` —— 1/24 个有
- `Light-Tool: KeyValue` —— 1/24 个有
- `Light-Tool: ShowText` —— 1/24 个有
- `Qwen2.5` —— 1/24 个有
- `ReferenceLatent` —— 1/24 个有
- `StringConcatenate` —— 1/24 个有
- `TextBox` —— 1/24 个有
- `图像缩放V2_孤海` —— 1/24 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 8 | 24 | 75% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 24 | 100% |
| 采样算法 | euler | - | 24 | 100% |
| 调度器 | simple | - | 24 | 100% |
| 重绘幅度 | 1 | 0.8 - 1 | 24 | 96% |
| 宽度 | 1080 | - | 1 | 100% |
| 高度 | 1920 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 25/24 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 8，24 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，24 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，24 个样本，一致性 100%
- 调度器 最常用 simple，24 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.8 - 1，24 个样本，取值集中（一致性 96%）
- 高发问题（25/24 个样本）：Steps较低可能导致细节不足
