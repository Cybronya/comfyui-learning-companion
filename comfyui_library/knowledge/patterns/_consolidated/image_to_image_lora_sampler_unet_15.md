---
name: image_to_image_lora_sampler_unet_15
type: Image To Image
frequency: 20
level: moderate
coverage: 0.8173
common_nodes: [CFGNorm, CLIPLoader, ImageScaleToTotalPixels, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/千问edit2509电影分镜制作（三个分镜头）_1985550462575431682.json, 图片生成/图生图/千问qwen一键服装替换_万物迁移工作流_1997614568350396418.json, 图片生成/图生图/去除光斑_过曝_欠曝修复_1995155032003764226.json, 图片生成/图生图/可视化摄像机角度调节_2039583466450325506.json, 图片生成/图生图/图片改变视角_2005454874915598337.json, 图片生成/图生图/图片视角转变_1989251290163187713.json, 图片生成/图生图/图片视角转变_1989550740198879233.json, 图片生成/图生图/图片视角转变_1991765325454716930.json, 图片生成/图生图/图片视角转变_2001990204246376449.json, 图片生成/图生图/图片视角转变_2016348615001772034.json, 图片生成/图生图/图片视角转变_2044301737418301442.json, 图片生成/图生图/图生图-视角转变_2041686193233989633.json, 图片生成/图生图/场景一键多角度切换Qwen-Edit-2509_1991347951650058242.json, 图片生成/图生图/控制相机角度_1991030936403943426.json, 图片生成/图生图/白模转材质_1991804491599278082.json, 图片生成/图生图/视角转换（新版）_1991125652569174017.json, 图片生成/图生图/镜头360_视角调整_1995146042221977602.json, 图片生成/文生图/人物超新全方位视角转换（新版）_1999135446234001410.json, 图片生成/文生图/全新多角度视角转换（新版）_1999145049768198145.json, 视频生成/图生视频/qwen多视角转换工作流_1987730871912435714.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_15

> 由 `engine/knowledge_consolidation` 从 20 个 workflow 归纳得出（图片生成/图生图/千问edit2509电影分镜制作（三个分镜头）_1985550462575431682.json、图片生成/图生图/千问qwen一键服装替换_万物迁移工作流_1997614568350396418.json、图片生成/图生图/去除光斑_过曝_欠曝修复_1995155032003764226.json、图片生成/图生图/可视化摄像机角度调节_2039583466450325506.json、图片生成/图生图/图片改变视角_2005454874915598337.json…）

- **类型**：Image To Image
- **样本数**：20
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 20 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
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
- `Image Comparer (rgthree)` —— 18/20 个有
- `easy imageSize` —— 16/20 个有
- `PreviewImage` —— 15/20 个有
- `CR Text` —— 2/20 个有
- `ShowText|pysssss` —— 2/20 个有
- `JWStringGetLine` —— 1/20 个有
- `LayerUtility: PurgeVRAM V2` —— 1/20 个有
- `ProcessString` —— 1/20 个有
- `QwenMultiangleCameraNode` —— 1/20 个有
- `RH_Captioner` —— 1/20 个有
- `TT_img_enc` —— 1/20 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 4 - 20 | 20 | 61% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 2.5 | 20 | 64% |
| 采样算法 | euler | - | 20 | 100% |
| 调度器 | simple | - | 20 | 95% |
| 重绘幅度 | 1 | 1 - 1 | 20 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 17/20 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 4 - 20，20 个样本
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 2.5，20 个样本
- 采样算法 最常用 euler，20 个样本，一致性 100%
- 调度器 最常用 simple，20 个样本，一致性 95%
- 重绘幅度 中位数 1，观测区间 1 - 1，20 个样本，取值集中（一致性 100%）
- 高发问题（17/20 个样本）：Steps较低可能导致细节不足
