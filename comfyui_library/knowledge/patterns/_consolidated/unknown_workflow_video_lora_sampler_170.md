---
name: unknown_workflow_video_lora_sampler_170
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.837417
common_nodes: [GetNode, ImageConcanate, ImageFromBatch, Int, LayerUtility: ImageScaleByAspectRatio V2, Seed, SetNode, SimpleMath+, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, WanAnimatePlus Bernini, WanAnimatePlus BlockSwap, WanAnimatePlus ContextOptions, WanAnimatePlus Decode, WanAnimatePlus LoraSelectMulti, WanAnimatePlus ModelLoader, WanAnimatePlus SamplerExtraArgs, WanAnimatePlus Samplerv2, WanAnimatePlus Schedulerv2, WanAnimatePlus SetBlockSwap, WanAnimatePlus SetLoRAs, WanAnimatePlus TextEncodeCached, WanAnimatePlus VAELoader, easy mathInt, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/交互式背景替换2_2080697137448443906.json, 视频生成/图生视频/多人场景选取双角色替换_2078455563666677762.json, 视频生成/图生视频/多人物交互指定替换_2075884144709689346.json, 视频生成/图生视频/影视二创角色替换1_2076558631444770818.json, 视频生成/图生视频/替换视频中的指定角色_2080945536378687490.json, 视频生成/图生视频/最新Bernini加速版人物替换_2074502633741705218.json, 视频生成/图生视频/最新影视二创多人场景选取角色替换_2078408351960100866.json, 视频生成/图生视频/最新影视二创视频角色替换_2078429040989528065.json, 视频生成/图生视频/最新影视二创视频角色替换漫剧_2078697075843362818.json, 视频生成/图生视频/来财蛙呱呱呱_2085649794168610818.json, 视频生成/图生视频/真人换卡通人物_2085656573984198657.json, 视频生成/图生视频/舞蹈动作迁移_2080234302566125570.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_170

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/图生视频/交互式背景替换2_2080697137448443906.json、视频生成/图生视频/多人场景选取双角色替换_2078455563666677762.json、视频生成/图生视频/多人物交互指定替换_2075884144709689346.json、视频生成/图生视频/影视二创角色替换1_2076558631444770818.json、视频生成/图生视频/替换视频中的指定角色_2080945536378687490.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 12 个 workflow 都包含：
- `GetNode`
- `ImageConcanate`
- `ImageFromBatch`
- `Int`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Seed`
- `SetNode`
- `SimpleMath+`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `WanAnimatePlus Bernini`
- `WanAnimatePlus BlockSwap`
- `WanAnimatePlus ContextOptions`
- `WanAnimatePlus Decode`
- `WanAnimatePlus LoraSelectMulti`
- `WanAnimatePlus ModelLoader`
- `WanAnimatePlus SamplerExtraArgs`
- `WanAnimatePlus Samplerv2`
- `WanAnimatePlus Schedulerv2`
- `WanAnimatePlus SetBlockSwap`
- `WanAnimatePlus SetLoRAs`
- `WanAnimatePlus TextEncodeCached`
- `WanAnimatePlus VAELoader`
- `easy mathInt`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 11/12 个有
- `Text` —— 11/12 个有
- `PreviewImage` —— 10/12 个有
- `easy imageCount` —— 10/12 个有
- `Float` —— 9/12 个有
- `Float to Int` —— 9/12 个有
- `ImageResizeKJv2` —— 6/12 个有
- `RHHiddenNodes` —— 6/12 个有
- `RH_Captioner` —— 6/12 个有
- `RMBG` —— 6/12 个有
- `TextConcatenate_UTK` —— 6/12 个有
- `easy indexAnything` —— 6/12 个有
- `Bjornulf_ShowInt` —— 5/12 个有
- `LayerUtility: PurgeVRAM V2` —— 4/12 个有
- `StringReplace` —— 4/12 个有
- `ExtractNFrames` —— 3/12 个有
- `ImageConcatMulti` —— 3/12 个有
- `RTXVideoSuperResolution` —— 3/12 个有
- `GoogleTranslateTextNode` —— 2/12 个有
- `PurgeVRAM_UTK` —— 2/12 个有
- `RH_Translator` —— 2/12 个有
- `CR Image Grid Panel` —— 1/12 个有
- `SaveImage` —— 1/12 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
