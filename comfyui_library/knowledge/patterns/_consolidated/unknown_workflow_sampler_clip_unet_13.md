---
name: unknown_workflow_sampler_clip_unet_13
type: Unknown Workflow
frequency: 30
level: moderate
coverage: 0.7847
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, Flux2Scheduler, GetImageSize, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/klein换头【可选  Bnanana pro】_2016044457656852482.json, 图片生成/图生图/pro_2026893876430118913.json, 图片生成/图生图/【Flux2 Klein】 双图编辑+换装lora版本_2030255334941528065.json, 图片生成/图生图/【Flux2 Klein】 （加密版）双图编辑+换装lora版本_2049724297060552705.json, 图片生成/图生图/【工作台】 双图编辑+换装lora版本（常规）_2075804075794456578.json, 图片生成/图生图/万物迁移（产品替换）Flux2Klein9b版本_2070089591029321729.json, 图片生成/图生图/产品_人物 换背景 光源一致F2-klein-9B_2083078402935975937.json, 图片生成/图生图/产品_人物_换背景_光源一致F2-klein-9B_2084994836385583105.json, 图片生成/图生图/产品_人物_换背景_光源一致F2-klein-9B_2085888858398486529.json, 图片生成/图生图/产品_人物_换背景_光源一致F2-klein-9B_2088506065381052418.json, 图片生成/图生图/产品_人物_换背景_光源一致F2-klein-9B_2091712412654329858.json, 图片生成/图生图/产品_人物_换背景_光源一致F2-klein-9B_2091844027921555458.json, 图片生成/图生图/产品_人物_换背景_光源一致F2-klein-9B_2092618498466996226.json, 图片生成/图生图/产品人物换背景光源一致F2-Klein-9B工作流_2084119585300766722.json, 图片生成/图生图/全能万物迁移 换装换脸 服装全品类换装 真实自然服饰迁移展示多图融合_2061681345826480129.json, 图片生成/图生图/最强万物迁移 f2k_9b_anything change clothes_2026650952215826434.json, 图片生成/图生图/最强产品_人物_换背景_光源一致任务一致F2-klein-9B加高清输出1_2085198054378000385.json, 图片生成/图生图/最强产品_人物_换背景_光源一致任务一致F2-klein-9B加高清输出1_2085207763952689154.json, 图片生成/图生图/电商产品换背景_2078457535203471361.json, 图片生成/图生图/真人转动漫+极速版 卡通动画角色设定+flux2+klein+9B+漫画手绘卡通网剧_2055088378185560066.json, 图片生成/图生图/真人转动漫+极速版+flux2+klein+9B+漫画手绘卡通网剧 角色设定_2055090424590675969.json, 图片生成/图生图/真人转动漫+极速版+卡通动画角色设定+flux2+klein+9B+漫画手绘卡通网剧+_2066338826917867521.json, 图片生成/图生图/真人转动漫的 flux klein_2025977265284190209.json, 图片生成/图生图/美女模特身材优化 Flux-2-klein-9B+胸部放大_2062735798742634497.json, 图片生成/图生图/美女模特身材优化+丰胸效果+胸部增强+Flux-2-klein-9B+胸部放大_2052265166510804994.json, 图片生成/图生图/美女模特身材优化+丰胸效果+胸部增强+Flux-2-klein-9B+胸部放大_2052296310446936066.json, 图片生成/图生图/苗条身材优化 美女模特身材优化+Flux-2-klein-9B+胸部放大 身形美体_2063795605662687234.json, 图片生成/图生图/（极速）真人转动漫漫画漫剧flux2+klein_2056934489481371649.json, 图片生成/文生图/f2_klein_9b_胸部放大器2.0_2026093999936774146.json, 图片生成/文生图/产品人物换背景光源一致F2-Klein-9B工作流_2084105106571743234.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_13

> 由 `engine/knowledge_consolidation` 从 30 个 workflow 归纳得出（图片生成/图生图/klein换头【可选  Bnanana pro】_2016044457656852482.json、图片生成/图生图/pro_2026893876430118913.json、图片生成/图生图/【Flux2 Klein】 双图编辑+换装lora版本_2030255334941528065.json、图片生成/图生图/【Flux2 Klein】 （加密版）双图编辑+换装lora版本_2049724297060552705.json、图片生成/图生图/【工作台】 双图编辑+换装lora版本（常规）_2075804075794456578.json…）

- **类型**：Unknown Workflow
- **样本数**：30
- **可信度**：中等可信
- **平均知识覆盖**：78%

## 共有节点

全部 30 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `Flux2Scheduler`
- `GetImageSize`
- `KSamplerSelect`
- `LoadImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 29/30 个有
- `EmptyFlux2LatentImage` —— 29/30 个有
- `LoraLoaderModelOnly` —— 29/30 个有
- `easy imageScaleDownToSize` —— 28/30 个有
- `Image Comparer (rgthree)` —— 26/30 个有
- `GetNode` —— 24/30 个有
- `SetNode` —— 24/30 个有
- `LayerUtility: ImageReel` —— 23/30 个有
- `LayerUtility: ImageReelComposit` —— 23/30 个有
- `Fast Groups Bypasser (rgthree)` —— 14/30 个有
- `easy cleanGpuUsed` —— 10/30 个有
- `Int` —— 6/30 个有
- `JWInteger` —— 5/30 个有
- `ImageConcanate` —— 3/30 个有
- `RH_Nano_Banana2_Image2Image` —— 2/30 个有
- `1hew_AnySwitchInt` —— 1/30 个有
- `Anything Everywhere3` —— 1/30 个有
- `DuckHideNode` —— 1/30 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/30 个有
- `Text Multiline` —— 1/30 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
