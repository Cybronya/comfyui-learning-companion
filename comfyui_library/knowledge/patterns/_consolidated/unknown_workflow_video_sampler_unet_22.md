---
name: unknown_workflow_video_sampler_unet_22
type: Unknown Workflow
frequency: 17
level: moderate
coverage: 0.546941
common_nodes: [BasicGuider, CLIPLoader, KSamplerSelect, LoadImage, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [图片生成/图生图/15步手动拟合特效增强，GIMM补帧战斗画面丝滑不卡_2116398340802965506.json, 图片生成/图生图/一人一鲸深海同游，8秒治愈大片直出_2117109958323036162.json, 图片生成/图生图/参考图变御剑飞行仙侠大片，云海穿行8秒直出_2117106745683304450.json, 图片生成/图生图/末日废土横屏宽画幅，沙暴追击8秒电影级直出_2116747481823404034.json, 图片生成/图生图/萌宠化身小厨师翻锅名场面，8秒治愈短片直出_2116748968242802690.json, 图片生成/图生图/雨夜功夫近身实战，打击气浪特效拉满直出8秒大片_2116746010159566850.json, 平台全量/参考图变深空机甲白刃大战，爆破光轨8秒直出_2117489747911340033.json, 平台全量/参考图变符文法术对轰横屏大片，金蓝冲击波8秒直出_2117491252278157313.json, 平台全量/参考图变雨夜霓虹追逐大片，全息光轨8秒直出_2117972380088889346.json, 平台全量/霓虹雨夜横屏宽画幅，全息都市追逐8秒直出_2117108464970457090.json, 视频生成/图生视频/MiniMax H3  15s全参_2084269888650174465.json, 视频生成/图生视频/MiniMax H3 I2V 图生视频 Fused ACC 8步 神奇工作流_2096909523062714369.json, 视频生成/图生视频/MiniMax H3 全能多参1280分辨率3_4Harness专用_2094567538721116161.json, 视频生成/图生视频/MiniMax H3 全能多参1280分辨率加速工作流_2085980820623413250.json, 视频生成/图生视频/MiniMax H3 全能多参DSW工作流Harness专用_2095550051505491970.json, 视频生成/图生视频/MiniMax H34步Lora超级加速版全能多图参考生视频_2085675097481891842.json, 视频生成/文生视频/MiniMax H3 I2V 图生视频 1280分辨率加速工作流_2085953821150367746.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_22

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（图片生成/图生图/15步手动拟合特效增强，GIMM补帧战斗画面丝滑不卡_2116398340802965506.json、图片生成/图生图/一人一鲸深海同游，8秒治愈大片直出_2117109958323036162.json、图片生成/图生图/参考图变御剑飞行仙侠大片，云海穿行8秒直出_2117106745683304450.json、图片生成/图生图/末日废土横屏宽画幅，沙暴追击8秒电影级直出_2116747481823404034.json、图片生成/图生图/萌宠化身小厨师翻锅名场面，8秒治愈短片直出_2116748968242802690.json…）

- **类型**：Unknown Workflow
- **样本数**：17
- **可信度**：中等可信
- **平均知识覆盖**：55%

## 共有节点

全部 17 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `KSamplerSelect`
- `LoadImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 16/17 个有
- `SetNode` —— 16/17 个有
- `MiniMaxH3ReferenceToVideo` —— 15/17 个有
- `ManualSigmas` —— 10/17 个有
- `SaveImage` —— 10/17 个有
- `孤海注释` —— 10/17 个有
- `BasicScheduler` —— 7/17 个有
- `ComfyMathExpression` —— 7/17 个有
- `PrimitiveFloat` —— 7/17 个有
- `ResolutionSelector` —— 7/17 个有
- `Text` —— 7/17 个有
- `LoraLoaderModelOnly` —— 6/17 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 6/17 个有
- `Label (rgthree)` —— 5/17 个有
- `SigmasGraph` —— 4/17 个有
- `ImageFromBatch` —— 3/17 个有
- `LoadAudio` —— 3/17 个有
- `VHS_LoadVideo` —— 3/17 个有
- `LoadVideo` —— 2/17 个有
- `MiniMaxH3ImageToVideo` —— 2/17 个有
- `LoraLoaderBypassModelOnly` —— 1/17 个有
- `ModelAttentionBackend` —— 1/17 个有
- `SolAttnMiniMax` —— 1/17 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
