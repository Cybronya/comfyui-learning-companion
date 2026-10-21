---
name: text_to_image_sampler_clip_unet_61
type: Text To Image
frequency: 8
level: moderate
coverage: 0.92075
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/anima-喵喵后宫-文生图_2084298158796009474.json, 图片生成/文生图/krea2 turbo文生图 极致美学_2069948625094012930.json, 图片生成/文生图/krea2-trubo-青绿水彩风格+水墨风格+光影效果彩色极简素描风格_2069757903887753218.json, 图片生成/文生图/krea2_turbo文生图+Lora+四倍高清放大_2080125976993947650.json, 图片生成/文生图/krea2基础工作流_2071862532075253761.json, 图片生成/文生图/krea2文生图+官方LORA_2069978232052600834.json, 图片生成/文生图/z-image文生图工作流（超写实）_2100510837722148865.json, 图片生成/文生图/提示词润色 文生图 图片编辑_2103111585429549057.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_61

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/anima-喵喵后宫-文生图_2084298158796009474.json、图片生成/文生图/krea2 turbo文生图 极致美学_2069948625094012930.json、图片生成/文生图/krea2-trubo-青绿水彩风格+水墨风格+光影效果彩色极简素描风格_2069757903887753218.json、图片生成/文生图/krea2_turbo文生图+Lora+四倍高清放大_2080125976993947650.json、图片生成/文生图/krea2基础工作流_2071862532075253761.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 6/8 个有
- `ConditioningZeroOut` —— 5/8 个有
- `ImageUpscaleWithModel` —— 4/8 个有
- `PreviewImage` —— 4/8 个有
- `UpscaleModelLoader` —— 4/8 个有
- `CR Text` —— 3/8 个有
- `Fast Groups Bypasser (rgthree)` —— 3/8 个有
- `AILab_QwenVL` —— 2/8 个有
- `CR Text Concatenate` —— 2/8 个有
- `QWEN_TextDisplay` —— 2/8 个有
- `CFGNorm` —— 1/8 个有
- `ImageFromBatch` —— 1/8 个有
- `JoinStringMulti` —— 1/8 个有
- `LayerColor: BrightnessContrastV2` —— 1/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/8 个有
- `LoadImage` —— 1/8 个有
- `RH_Nano_Banana_Image2Image` —— 1/8 个有
- `SaveAnimatedWEBP` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 896 - 1920 | 8 | 73% |
| 高度 | 1408 | 720 - 1920 | 8 | 72% |
| 采样步数 | 8 | 6 - 30 | 8 | 32% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 8 | 28% |
| 采样算法 | euler | - | 8 | 88% |
| 调度器 | simple | - | 8 | 62% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 896 - 1920，8 个样本
- 高度 中位数 1408，观测区间 720 - 1920，8 个样本
- 采样步数 中位数 8，观测区间 6 - 30，8 个样本，取值分散，一致性仅 32%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，8 个样本，取值分散，一致性仅 28%
- 采样算法 最常用 euler，8 个样本，一致性 88%
- 调度器 最常用 simple，8 个样本，一致性 62%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（9/8 个样本）：Steps较低可能导致细节不足
