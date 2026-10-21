---
name: text_to_image_sampler_clip_unet_11
type: Text To Image
frequency: 19
level: moderate
coverage: 0.939789
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-image文生图，二次元校园女生风格Lora_1998998879238508546.json, 图片生成/文生图/Z-image最强文生图模型_1994953430059954178.json, 图片生成/文生图/Z-image照片级超真实人物_2008470665782894594.json, 图片生成/文生图/Z-image生图_2102776816992866305.json, 图片生成/文生图/Z-image真实感文生图急速出图_1993918066069356545.json, 图片生成/文生图/Z-image美女IP角色工作流（单图训练的lora）_2008089851932975106.json, 图片生成/文生图/Zimage_Turbo尺寸控制器版_2073283589403402242.json, 图片生成/文生图/Zimage_Turbo经典版_2047589392318992385.json, 图片生成/文生图/api-z-image_1995157591246430209.json, 图片生成/文生图/boogu turbo批量文生图_2070386922110930945.json, 图片生成/文生图/boogu turbo文生图批量版_2070336788392144897.json, 图片生成/文生图/boogu turbo文生图批量版_2070422555663622146.json, 图片生成/文生图/boogu turbo文生图批量版_2070469626550644737.json, 图片生成/文生图/krea2文生图批量版_2070339623888441346.json, 图片生成/文生图/krea2文生图批量版_2070388445238878210.json, 图片生成/文生图/krea2文生图批量版_2070421570203508737.json, 图片生成/文生图/krea2文生图批量版_2070468131897827330.json, 图片生成/文生图/动漫柔和光（Anima）_2073031688103485441.json, 图片生成/文生图/文生图（Z-image，带lora）_1998357719558029314.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_11

> 由 `engine/knowledge_consolidation` 从 19 个 workflow 归纳得出（图片生成/文生图/Z-image文生图，二次元校园女生风格Lora_1998998879238508546.json、图片生成/文生图/Z-image最强文生图模型_1994953430059954178.json、图片生成/文生图/Z-image照片级超真实人物_2008470665782894594.json、图片生成/文生图/Z-image生图_2102776816992866305.json、图片生成/文生图/Z-image真实感文生图急速出图_1993918066069356545.json…）

- **类型**：Text To Image
- **样本数**：19
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 19 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 17/19 个有
- `CR Text` —— 11/19 个有
- `PromptBatchQueue` —— 9/19 个有
- `HAIGC_SaveImagesToZip` —— 8/19 个有
- `LoraLoaderModelOnly` —— 7/19 个有
- `Int` —— 4/19 个有
- `LayerUtility: TextJoinV2` —— 2/19 个有
- `PrimitiveStringMultiline` —— 2/19 个有
- `MuyeSizeSelector` —— 1/19 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 30 | 19 | 52% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 19 | 42% |
| 采样算法 | euler | - | 19 | 63% |
| 调度器 | simple | - | 19 | 89% |
| 重绘幅度 | 1 | 1 - 1 | 19 | 100% |
| 宽度 | 1024 | 1024 - 2416 | 19 | 72% |
| 高度 | 1536 | 1024 - 1920 | 19 | 82% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/19 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 30，19 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，19 个样本，取值分散，一致性仅 42%
- 采样算法 最常用 euler，19 个样本，一致性 63%
- 调度器 最常用 simple，19 个样本，一致性 89%
- 重绘幅度 中位数 1，观测区间 1 - 1，19 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1024 - 2416，19 个样本
- 高度 中位数 1536，观测区间 1024 - 1920，19 个样本，取值集中（一致性 82%）
- 高发问题（10/19 个样本）：Steps较低可能导致细节不足
