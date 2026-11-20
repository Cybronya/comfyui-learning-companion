---
name: unknown_workflow_upscale_lora_clip
type: Unknown Workflow
frequency: 21
level: moderate
coverage: 0.816905
common_nodes: [CLIPTextEncode, DualCLIPLoader, LayerColor: ColorAdapter, LayerUtility: ImageScaleByAspectRatio V2, LoraLoaderModelOnly, SaveImage, SeedVR2, TeaCache, UNETLoader, UltimateSDUpscale, UpscaleModelLoader, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/SEEDVR2放大4K_2004002122272260097.json, 图片生成/图生图/放大-无损_2019952994254594049.json, 图片生成/图生图/最强高清放大_2073383259416915969.json, 图片生成/图生图/最强高清放大还原_2059995705959342081.json, 图片生成/图生图/最强高清放大还原_2059998341546733570.json, 图片生成/图生图/最强高清放大还原_2068260565579026433.json, 图片生成/图生图/标哥_5K高清放大（不变图面结构）_2011035910145581057.json, 图片生成/图生图/超强高清放大_2072700587124281345.json, 图片生成/图生图/超强高清放大_2073217830027350018.json, 图片生成/图生图/超强高清放大_2073593372786388994.json, 图片生成/图生图/超级好用的高清放大工作流_1995444676809383938.json, 图片生成/图生图/高清放大-SeedVR2 Video Upscale+SD放大_2009255322887659521.json, 图片生成/图生图/高清放大-SeedVR2+Flux+SD放大【测试】_2048455426366251009.json, 图片生成/图生图/高清放大-SeedVR2+Flux+SD放大（5分钟）_1968194524256284674.json, 图片生成/图生图/高清放大_1977240953708793857.json, 图片生成/图生图/高清放大工作流（佳）_1964694750018289665.json, 图片生成/图生图/高清放大流-好用_1986969329310830594.json, 图片生成/图生图/高清放大流最新版_1950100460037390337.json, 图片生成/图生图/高清放大还原2560_4768_2031256830462136322.json, 图片生成/文生图/高清放大流-好用（干净版）_2104395854693093377.json, 图片生成/文生图/高清放大流最新版（干净版）_2104394861406408705.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_clip

> 由 `engine/knowledge_consolidation` 从 21 个 workflow 归纳得出（图片生成/图生图/SEEDVR2放大4K_2004002122272260097.json、图片生成/图生图/放大-无损_2019952994254594049.json、图片生成/图生图/最强高清放大_2073383259416915969.json、图片生成/图生图/最强高清放大还原_2059995705959342081.json、图片生成/图生图/最强高清放大还原_2059998341546733570.json…）

- **类型**：Unknown Workflow
- **样本数**：21
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 21 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `LayerColor: ColorAdapter`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoraLoaderModelOnly`
- `SaveImage`
- `SeedVR2`
- `TeaCache`
- `UNETLoader`
- `UltimateSDUpscale`
- `UpscaleModelLoader`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 20/21 个有
- `LoadImage` —— 20/21 个有
- `SeedVR2BlockSwap` —— 20/21 个有
- `Get Image Size` —— 19/21 个有
- `ImageResize+` —— 19/21 个有
- `ImageScaleToTotalPixels` —— 19/21 个有
- `PreviewImage` —— 18/21 个有
- `easy compare` —— 18/21 个有
- `easy ifElse` —— 18/21 个有
- `Fast Groups Bypasser (rgthree)` —— 8/21 个有
- `Image Lucy Sharpen` —— 2/21 个有
- `ImageUpscaleWithModel` —— 2/21 个有
- `DisplayImageFromURL` —— 1/21 个有
- `ImpactCompare` —— 1/21 个有
- `LoraLoader` —— 1/21 个有
- `easy showAnything` —— 1/21 个有
- `孤海图像裁剪按比例` —— 1/21 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.8 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
