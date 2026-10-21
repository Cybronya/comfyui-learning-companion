---
name: text_to_image_lora_sampler_clip_16
type: Text To Image
frequency: 26
level: strong
coverage: 0.571654
common_nodes: [AILab_QwenVL, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, Fast Groups Bypasser (rgthree), FluxGuidance, JjkText, JoinStrings, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, Lora Loader, SaveImage, UNETLoader, VAEDecode, VAELoader, easy showAnything]
problems: []
missing: [LayerUtility: ImageScaleByAspectRatio V2, Lora Loader]
members: [图片生成/文生图/1955452266036674562.json, 图片生成/文生图/HAO- CCD加强3张竖屏（反推_文生）_2066047288212025346.json, 图片生成/文生图/HAO-CCD-V2_2066852559930871809.json, 图片生成/文生图/HAO-CCD氛围感_2066058829959360514.json, 图片生成/文生图/Zimage 无滤真实_v2 文生图+图生图（反推）工作流_2027172387564822530.json, 图片生成/文生图/Zimage 真实皮肤 文生图+图生图（反推）_2058137530037522433.json, 图片生成/文生图/Zimage 真实皮肤 文生图+图生图（反推）_2065623548969971714.json, 图片生成/文生图/Zimage 真实皮肤 文生图+图生图（反推）_2068187611491028993.json, 图片生成/文生图/Zimage 真实皮肤 文生图+图生图（反推）_2068189551646035969.json, 图片生成/文生图/Zimage 真实皮肤 文生图+图生图（反推）_2069450536801361922.json, 图片生成/文生图/Zimage 真实皮肤 文生图+图生图（反推）_2070426110814408705.json, 图片生成/文生图/Zimage 真实皮肤 文生图+图生图（反推）_2073779891207761921.json, 图片生成/文生图/Zimage 真实皮肤 文生图+图生图（反推）_2075240742649421825.json, 图片生成/文生图/Zimage 真实皮肤 文生图+图生图（反推）_2077031681701277697.json, 图片生成/文生图/Zimage 真实皮肤 文生图+图生图（反推）_2078869906430447618.json, 图片生成/文生图/Zimage 真实皮肤 文生图+图生图（反推）_2080265618636492801.json, 图片生成/文生图/Zimage 真实皮肤 文生图+图生图（反推）_2080326234017460226.json, 图片生成/文生图/Zimage 真实皮肤 文生图+图生图（反推）_2080330261774028801.json, 图片生成/文生图/Zimage 真实皮肤 文生图+图生图（反推）_2080631287123107842.json, 图片生成/文生图/Zimage 真实皮肤 文生图+图生图（反推）_2080681183788224514.json, 图片生成/文生图/Zimage 真实皮肤 文生图+图生图（反推）工作流_2056945900718739457.json, 图片生成/文生图/Zimage增强真实皮肤文生图图生图反推_2064505010330890241.json, 图片生成/文生图/Zimage真实皮肤文生图图生图反推_2063478682601222146.json, 图片生成/文生图/文生图_图生图_全能图片三合一工作流_2069693848510623745.json, 图片生成/文生图/文生图_图生图_全能图片三合一工作流_2069699625069666305.json, 数字人/数字人/Zimage+真实皮肤+文生图+图生图（反推）_2091817479264886785.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_16

> 由 `engine/knowledge_consolidation` 从 26 个 workflow 归纳得出（图片生成/文生图/1955452266036674562.json、图片生成/文生图/HAO- CCD加强3张竖屏（反推_文生）_2066047288212025346.json、图片生成/文生图/HAO-CCD-V2_2066852559930871809.json、图片生成/文生图/HAO-CCD氛围感_2066058829959360514.json、图片生成/文生图/Zimage 无滤真实_v2 文生图+图生图（反推）工作流_2027172387564822530.json…）

- **类型**：Text To Image
- **样本数**：26
- **可信度**：强结论
- **平均知识覆盖**：57%

## 共有节点

全部 26 个 workflow 都包含：
- `AILab_QwenVL`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `FluxGuidance`
- `JjkText`
- `JoinStrings`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `Lora Loader`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere` —— 23/26 个有
- `CFGNorm` —— 23/26 个有
- `GetNode` —— 23/26 个有
- `LayerColor: AutoAdjust` —— 23/26 个有
- `SetNode` —— 23/26 个有
- `Float` —— 20/26 个有
- `TT_img_enc` —— 19/26 个有
- `孤海注释` —— 19/26 个有
- `easy saveText` —— 4/26 个有
- `Image Comparer (rgthree)` —— 3/26 个有
- `RH_RhartImageNG31FlashImageToImage` —— 3/26 个有
- `ImpactSwitch` —— 2/26 个有
- `Int` —— 2/26 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 15 | 15 - 15 | 26 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 26 | 100% |
| 采样算法 | res_2s | - | 26 | 81% |
| 调度器 | FlowMatchEulerDiscreteScheduler | - | 26 | 92% |
| 重绘幅度 | 1 | 1 - 1 | 26 | 100% |
| 宽度 | 1536 | 1080 - 1536 | 26 | 87% |
| 高度 | 1960 | 1560 - 1960 | 26 | 93% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 15，观测区间 15 - 15，26 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，26 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_2s，26 个样本，一致性 81%
- 调度器 最常用 FlowMatchEulerDiscreteScheduler，26 个样本，一致性 92%
- 重绘幅度 中位数 1，观测区间 1 - 1，26 个样本，取值集中（一致性 100%）
- 宽度 中位数 1536，观测区间 1080 - 1536，26 个样本，取值集中（一致性 87%）
- 高度 中位数 1960，观测区间 1560 - 1960，26 个样本，取值集中（一致性 93%）
- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: ImageScaleByAspectRatio V2、Lora Loader
