# QwenImage21Cache

## 节点类型

`QwenImage21Cache`

## 分类

Model Optimization（Qwen Image 2.1 专属）

## 作用

对 Qwen Image 2.1 的模型/编码器做缓存管理，避免重复计算，
多步工作流（文生图+编辑多分支）里显著提速。

## 参数（统计自 404 个真实 workflow，131 次出现）

| 参数 | 说明 | 实测分布 |
|---|---|---|
| cache_mode | 缓存模式 | 99% 为 auto；个别 gpu |
| 其他 | preset 类 | default |

## 常见问题与风险

- auto 模式基本免维护；显存充裕时可忽略本节点，
  显存紧张时它能减少重复编码开销。
- 属于社区/加速整合包常用节点，纯净官方流里通常不出现。

## 可信度

Generated（2026-10-06，参数分布实测；作用描述推断自使用场景，把握较低）TODO(待验证)
