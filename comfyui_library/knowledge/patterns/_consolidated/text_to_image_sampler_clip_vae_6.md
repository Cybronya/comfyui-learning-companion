---
name: text_to_image_sampler_clip_vae_6
type: Text To Image
frequency: 17
level: strong
coverage: 0.946353
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Nunchaku-Qwen-Image文生图lora版_1982417831478345730.json, 图片生成/文生图/Z-Image文生图_2094304743563812866.json, 图片生成/文生图/Z-Image文生图基础工作流_2004808008284733442.json, 图片生成/文生图/Z-image + LoRA 文生图工作流_2058875529981415425.json, 图片生成/文生图/Z-image 全能模型_1994451694316625922.json, 图片生成/文生图/Z-image 文生图工作流（含加速器）_2046950465908252673.json, 图片生成/文生图/Z-image-MJ风格图像生成_2041506818840596482.json, 图片生成/文生图/Z-image-turbo 2.5D奶油风格生图Lora_2055258113829294081.json, 图片生成/文生图/Z-image-turbo基础文生图【用于绘世comfyui批量管理系统】_2089190207693344769.json, 图片生成/文生图/Z-image文生图V2（Lora）_2026213692454477825.json, 图片生成/文生图/Z_image_turbo快速文生图 自用版_2097176754392756226.json, 图片生成/文生图/Z_image_turbo快速文生图_2051577152918835202.json, 图片生成/文生图/ki_krea2人物四视图_2107463809878282242.json, 图片生成/文生图/krea2 Lora文生图加英伟达rtx nodes高清放大_2074689431730221057.json, 图片生成/文生图/krea2基础文生图_2098922890111574018.json, 图片生成/文生图/krea2基础文生图_2098981510849327105.json, 图片生成/文生图/krea2基础文生图_2099657569232056322.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_vae_6

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（图片生成/文生图/Nunchaku-Qwen-Image文生图lora版_1982417831478345730.json、图片生成/文生图/Z-Image文生图_2094304743563812866.json、图片生成/文生图/Z-Image文生图基础工作流_2004808008284733442.json、图片生成/文生图/Z-image + LoRA 文生图工作流_2058875529981415425.json、图片生成/文生图/Z-image 全能模型_1994451694316625922.json…）

- **类型**：Text To Image
- **样本数**：17
- **可信度**：强结论
- **平均知识覆盖**：95%

## 共有节点

全部 17 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `UNETLoader` —— 16/17 个有
- `ConditioningZeroOut` —— 13/17 个有
- `LoraLoaderModelOnly` —— 10/17 个有
- `PreviewImage` —— 10/17 个有
- `RTXVideoSuperResolution` —— 5/17 个有
- `EmptyImage` —— 4/17 个有
- `Fast Groups Muter (rgthree)` —— 1/17 个有
- `LayerUtility: PurgeVRAM V2` —— 1/17 个有
- `NunchakuQwenImageDiTLoader` —— 1/17 个有
- `NunchakuQwenImageLoraLoader` —— 1/17 个有
- `NunchakuQwenImageLoraStack` —— 1/17 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 8 - 10 | 17 | 89% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 17 | 100% |
| 采样算法 | euler | - | 17 | 76% |
| 调度器 | simple | - | 17 | 88% |
| 重绘幅度 | 1 | 1 - 1 | 17 | 100% |
| 宽度 | 1024 | 512 - 1920 | 17 | 69% |
| 高度 | 1536 | 512 - 2048 | 17 | 69% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/17 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 8 - 10，17 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，17 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，17 个样本，一致性 76%
- 调度器 最常用 simple，17 个样本，一致性 88%
- 重绘幅度 中位数 1，观测区间 1 - 1，17 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 512 - 1920，17 个样本
- 高度 中位数 1536，观测区间 512 - 2048，17 个样本
- 高发问题（9/17 个样本）：Steps较低可能导致细节不足
