---
name: unknown_workflow_upscale_lora_clip
type: Unknown Workflow
frequency: 35
level: moderate
coverage: 0.824743
common_nodes: [CLIPTextEncode, DualCLIPLoader, LayerColor: ColorAdapter, LayerUtility: ImageScaleByAspectRatio V2, LoraLoaderModelOnly, SaveImage, SeedVR2, TeaCache, UltimateSDUpscale, UpscaleModelLoader, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/SEEDVR2放大4K_2004002122272260097.json, 图片生成/图生图/放大-无损_2019952994254594049.json, 图片生成/图生图/最强高清放大_2073383259416915969.json, 图片生成/图生图/最强高清放大还原_2059995705959342081.json, 图片生成/图生图/最强高清放大还原_2059998341546733570.json, 图片生成/图生图/最强高清放大还原_2068260565579026433.json, 图片生成/图生图/标哥_5K高清放大（不变图面结构）_2011035910145581057.json, 图片生成/图生图/超强高清放大_2072700587124281345.json, 图片生成/图生图/超强高清放大_2073217830027350018.json, 图片生成/图生图/超强高清放大_2073593372786388994.json, 图片生成/图生图/超级好用的高清放大工作流_1995444676809383938.json, 图片生成/图生图/高清放大-SeedVR2 Video Upscale+SD放大_2009255322887659521.json, 图片生成/图生图/高清放大-SeedVR2+Flux+SD放大【测试】_2048455426366251009.json, 图片生成/图生图/高清放大-SeedVR2+Flux+SD放大（5分钟）_1968194524256284674.json, 图片生成/图生图/高清放大_1977240953708793857.json, 图片生成/图生图/高清放大工作流（佳）_1964694750018289665.json, 图片生成/图生图/高清放大流-好用_1986969329310830594.json, 图片生成/图生图/高清放大流最新版_1950100460037390337.json, 图片生成/图生图/高清放大还原2560_4768_2031256830462136322.json, 图片生成/文生图/高清放大流-好用（干净版）_2104395854693093377.json, 图片生成/文生图/高清放大流最新版（干净版）_2104394861406408705.json, 平台全量/tpgq_2010988237489180673.json, 平台全量/一键极致图像高清修复_1955486881419071489.json, 平台全量/最强高清放大_2073391439568003073.json, 平台全量/最强高清放大还原_1959981937114951682.json, 平台全量/最强高清放大还原_2059481130537148418.json, 平台全量/最强高清放大还原_2064716761303445506.json, 平台全量/最强高清放大还原_2067566271834710017.json, 平台全量/最强高清放大还原_2068980451871645697.json, 平台全量/最强高清放大还原_2070782852035342337.json, 平台全量/最强高清放大还原_2073073207845941249.json, 平台全量/最强高清放大还原（极速版）_1960353811485306882.json, 平台全量/高清放大工作流_1963146964504391682.json, 平台全量/高清放大流 超级好用_1979024426186477570.json, 平台全量/高清放大还原2560_4768_2067861571895910402.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_clip

> 由 `engine/knowledge_consolidation` 从 35 个 workflow 归纳得出（图片生成/图生图/SEEDVR2放大4K_2004002122272260097.json、图片生成/图生图/放大-无损_2019952994254594049.json、图片生成/图生图/最强高清放大_2073383259416915969.json、图片生成/图生图/最强高清放大还原_2059995705959342081.json、图片生成/图生图/最强高清放大还原_2059998341546733570.json…）

- **类型**：Unknown Workflow
- **样本数**：35
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 35 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `LayerColor: ColorAdapter`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoraLoaderModelOnly`
- `SaveImage`
- `SeedVR2`
- `TeaCache`
- `UltimateSDUpscale`
- `UpscaleModelLoader`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 34/35 个有
- `LoadImage` —— 34/35 个有
- `UNETLoader` —— 34/35 个有
- `Get Image Size` —— 33/35 个有
- `ImageResize+` —— 33/35 个有
- `ImageScaleToTotalPixels` —— 33/35 个有
- `SeedVR2BlockSwap` —— 33/35 个有
- `easy compare` —— 31/35 个有
- `easy ifElse` —— 31/35 个有
- `PreviewImage` —— 28/35 个有
- `Fast Groups Bypasser (rgthree)` —— 17/35 个有
- `Image Lucy Sharpen` —— 2/35 个有
- `ImageUpscaleWithModel` —— 2/35 个有
- `ImpactCompare` —— 2/35 个有
- `easy showAnything` —— 2/35 个有
- `DisplayImageFromURL` —— 1/35 个有
- `LoraLoader` —— 1/35 个有
- `RHHiddenNodes` —— 1/35 个有
- `孤海图像裁剪按比例` —— 1/35 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.8 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
